class Graph(object):

    def __init__(self):
        self.adj_list = {}
        self.nodes = []
        self.node_val_map = {}
        self.val_node_map = {}
        self.locations = {}
        self.edge_costs = {}


class CPGraph(object):

    def __init__(self, graph):
        self.orig_graph = graph
        self.odd_nodes = []
        self.adj_list = {}

    def remove_edges(self, visited):
        for e in visited:
            self.remove_edge(e)

    def remove_edge(self, edge):
        u, v = edge
        self._remove_edge_op(u, v)
        self._remove_edge_op(v, u)

    def _remove_edge_op(self, v1, v2):
        for a, d in self.adj_list[v1]:
            if a == v2:
                self.adj_list[v1].remove((a, d))
                break

    def add_edge(self, edge):
        u, v = edge
        d = 0
        if (u, v) in self.orig_graph.edge_costs.keys():
            d = self.orig_graph.edge_costs[(u, v)]
        elif (v, u) in self.orig_graph.edge_costs.keys():
            d = self.orig_graph.edge_costs[(v, u)]

        self._add_edge_op(u, v, d)
        self._add_edge_op(v, u, d)

    def _add_edge_op(self, v1, v2, d):
        if v1 not in self.adj_list.keys():
            self.adj_list[v1] = []
        self.adj_list[v1].append((v2, d))

    # A DFS based function to count reachable vertices from v
    def dfs_count(self, v, visited):
        count = 1
        visited.append(v)
        for i, d in self.adj_list[v]:
            if i not in visited:
                count = count + self.dfs_count(i, visited)
        return count

    # The function to check if edge u-v can be considered as next edge in
    # Euler Tour
    def is_valid_next_edge(self, u, v):
        # The edge u-v is valid in one of the following two cases:

        #  1) If v is the only adjacent vertex of u
        if len(self.adj_list[u]) == 1:
            return True
        else:
            '''
             2) If there are multiple adjacents, then u-v is not a bridge
                 Do following steps to check if u-v is a bridge

            2.a) count of vertices reachable from u'''
            visited = []
            count1 = self.dfs_count(u, visited)

            '''2.b) Remove edge (u, v) and after removing the edge, count
                vertices reachable from u'''
            self.remove_edge((u, v))
            visited = []
            count2 = self.dfs_count(u, visited)

            # 2.c) Add the edge back to the graph
            self.add_edge((u, v))

            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            return False if count1 > count2 else True


def convert_own_to_cp(graph, edges):
    cp_graph = CPGraph(graph)

    covered = set()
    for u, v in edges:
        if (u, v) in covered or (v, u) in covered:
            continue
        cp_graph.add_edge((u, v))
        covered.add((u, v))

    for n, l in cp_graph.adj_list.items():
        if len(l) % 2 != 0:
            cp_graph.odd_nodes.append(n)

    return cp_graph


def convert_osnx_to_own(G):

    graph = Graph()
    for i, node in enumerate(G.nodes()):
        graph.node_val_map[node] = i+1
        graph.val_node_map[i+1] = node
        graph.nodes.append(i+1)
        graph.locations[i+1] = (G.node[node]['x'], G.node[node]['y'])

    covered = set()
    for u, v, data in G.edges(data=True):
        new_u, new_v = graph.node_val_map[u], graph.node_val_map[v]
        if (new_u, new_v) in covered or (new_v, new_u) in covered:
            continue
        dist = int(data["length"])

        if new_u not in graph.adj_list.keys():
            graph.adj_list[new_u] = []
        if new_v not in graph.adj_list.keys():
            graph.adj_list[new_v] = []
        graph.adj_list[new_u].append((new_v, dist))
        graph.adj_list[new_v].append((new_u, dist))

        graph.edge_costs[(new_u, new_v)] = dist
        graph.edge_costs[(new_v, new_u)] = dist

        covered.add((new_u, new_v))
    return graph

