import copy
import itertools
import random
import dijkstra
import network


def get_tour_and_cost(graph, priority_path):
    """ Find a tour covering each edge at least once
    and the time taken for the tour """

    mod_graph = _make_eularian(graph)
    return _eulerian_path(mod_graph, priority_path)


def _euler_util(graph, u, route):
    cost = 0
    # Recur for all the vertices adjacent to this vertex
    for v, d in graph.adj_list[u]:
        # If edge u-v is not removed and it's a a valid next edge
        if graph.is_valid_next_edge(u, v):
            route.append(v)
            cost = cost + d
            graph.remove_edge((u, v))
            cost += _euler_util(graph, v, route)
    return cost


def _eulerian_path(graph, priority_path):
    """ Find Eulerian path """
    cost = 0
    route = []
    pp_in_cluster = _order_nodes(graph, priority_path)
    print('Priority path in cluster: {}'.format(pp_in_cluster))
    if len(pp_in_cluster) > 0:
        last = -1
        for i in range(0, len(pp_in_cluster)-1):
            if graph.is_valid_next_edge(pp_in_cluster[i], pp_in_cluster[i+1]):
                route.append(pp_in_cluster[i])
                cost = cost + graph.orig_graph.edge_costs[(pp_in_cluster[i], pp_in_cluster[i+1])]
                graph.remove_edge((pp_in_cluster[i], pp_in_cluster[i+1]))
            else:
                last = i
                break

        node = pp_in_cluster[last]
    else:
        node = random.choice([k for k in graph.adj_list.keys()])
    route.append(node)
    cost += _euler_util(graph, node, route)
    return route, cost


def _order_nodes(graph, path):
    nodes = []
    for k in graph.adj_list.keys():
        nodes.append(k)
    C = [0]*(len(nodes)+len(path)+1)
    C[len(path)] = -1
    LB = len(path) + 1
    for i in range(0, len(nodes)):
        try:
            x = path.index(nodes[i])
        except ValueError:
            C[LB] = nodes[i]
            LB += 1
        else:
            C[x] = nodes[i]
    q = [list(y) for x, y in itertools.groupby(C, lambda z: z == -1) if not x]
    spl = [list(y) for x, y in itertools.groupby(q[0], lambda z: z == 0) if not x]
    maxL = 0
    maxS = []
    for i in range(0, len(spl)):
        if len(spl[i]) > maxL:
            maxL = len(spl[i])
            maxS = spl[i]
    return maxS


def _build_node_pairs(graph):
    """ Builds all possible odd node pairs. """
    return [x for x in itertools.combinations(graph.odd_nodes, 2)]


def _unique_pairs(items):
    """ Generate sets of unique pairs of odd nodes. """
    for item in items[1:]:
        pair = items[0], item
        leftovers = [a for a in items if a not in pair]
        if leftovers:
            # Python 2.7 version? Are they equivalent??
            for tail in _unique_pairs(leftovers):
                yield [pair] + tail
        else:
            yield [pair]


def _find_node_pair_solutions(graph, node_pairs):
    """ Return path and cost for all node pairs in the path sets. """
    node_pair_solutions = {}
    for node_pair in node_pairs:
        if node_pair not in node_pair_solutions:
            cost, path = dijkstra.find(graph, node_pair[0], node_pair[1])
            node_pair_solutions[node_pair] = (cost, path)
            # Also store the reverse pair
            node_pair_solutions[node_pair[::-1]] = (cost, path[::-1])
    return node_pair_solutions


def _find_minimum_path_set(pair_sets, pair_solutions):
    """ Return cheapest cost & route for all sets of node pairs. """
    cheapest_set = None
    min_cost = float('inf')
    min_route = []
    loop = 0
    for pair_set in pair_sets:
        if loop >= 2000:
            break
        set_cost = sum(pair_solutions[pair][0] for pair in pair_set)
        if set_cost < min_cost:
            cheapest_set = pair_set
            min_cost = set_cost
            min_route = [pair_solutions[pair][1] for pair in pair_set]
        loop += 1

    return cheapest_set, min_route


def _add_new_edges(graph, min_route):
    """ Return new graph w/ new edges extracted from minimum route. """
    new_graph = copy.deepcopy(graph)
    for node in min_route:
        for i in range(len(node) - 1):
            start, end = node[i], node[i + 1]
            new_graph.add_edge((start, end))  # Append new edges
    return new_graph


def _make_eularian(graph):
    """ Add necessary paths to the graph such that it becomes Eularian. """

    print('Building possible odd node pairs...')
    node_pairs = list(_build_node_pairs(graph))
    print('\t({} pairs)'.format(len(node_pairs)))

    print('Finding pair solutions...')
    pair_solutions = _find_node_pair_solutions(graph, node_pairs)
    print('\t({} solutions)'.format(len(pair_solutions)))

    print('Building path sets...')
    pair_sets = (x for x in _unique_pairs(graph.odd_nodes))

    print('Finding cheapest route...')
    cheapest_set, min_route = _find_minimum_path_set(pair_sets, pair_solutions)
    print('Adding new edges...')
    return _add_new_edges(graph, min_route)  # Add our new edges


if __name__ == '__main__':

    g = network.Graph()
    test_graph = network.CPGraph(g)
    test_graph.adj_list = {
        1: [(140, 154)],
        4: [(79, 414), (82, 236)],
        133: [(82, 108), (91, 210), (139, 335)],
        6: [(115, 169), (96, 160)],
        8: [(110, 220)],
        138: [(79, 343), (82, 354), (136, 107)],
        139: [(26, 114), (101, 180), (133, 335)],
        140: [(1, 154), (115, 245)],
        141: [(78, 12)],
        142: [(110, 516), (124, 110), (136, 218)],
        20: [(75, 114), (23, 132), (28, 94)],
        23: [(20, 132)],
        24: [(28, 134)],
        26: [(104, 312), (29, 232), (139, 114)],
        28: [(11, 89), (20, 94), (24, 134)],
        29: [(26, 232), (124, 34), (98, 275)],
        44: [(71, 751)],
        45: [(124, 259), (115, 63), (71, 77)],
        46: [(92, 41)],
        136: [(121, 317), (138, 107), (142, 218)],
        11: [(28, 89), (78, 81)],
        71: [(44, 751), (45, 77), (115, 41)],
        75: [(20, 114), (98, 268), (100, 37)],
        78: [(11, 81), (141, 12)],
        79: [(4, 414), (138, 343)],
        82: [(4, 236), (133, 108), (138, 354)],
        84: [(92, 296)],
        91: [(101, 427), (133, 210)],
        92: [(46, 41), (84, 296), (96, 184)],
        96: [(6, 160), (92, 184), (127, 429)],
        98: [(29, 275), (75, 268), (104, 225)],
        100: [(75, 37)],
        101: [(91, 427), (139, 180)],
        104: [(26, 312), (98, 225), (121, 54)],
        110: [(8, 220), (121, 267), (142, 516)],
        115: [(6, 169), (45, 63), (71, 41), (140, 245)],
        121: [(104, 54), (110, 267), (136, 317)],
        124: [(29, 34), (45, 259), (142, 110)],
        127: [(96, 429)]
    }

    for n, l in test_graph.adj_list.items():
        if len(l) % 2 != 0:
            test_graph.odd_nodes.append(n)

    print(get_tour_and_cost(test_graph))
