import floyd_warshall, clustering, chinese_postman, network, dijkstra


class TourPlanner(object):

    def __init__(self, graph, k):
        self.graph = graph
        self.k = k

    def cluster(self):
        print('Finding distances and paths....')
        distances = floyd_warshall.find_distances(self.graph)

        print('Finding clusters of edges....')
        clusters = clustering.cluster(self.graph, self.k, distances)

        return clusters

    def plan(self, clusters, priority_path):

        tours = {}
        times = {}

        for i, cluster in enumerate(clusters):
            cp_graph = network.convert_own_to_cp(self.graph, cluster)
            print('\nFinding tour in cluster {} using Chinese Postman Problem....\n'.format(i))
            tours[i], times[i] = chinese_postman.get_tour_and_cost(cp_graph, priority_path)

        return tours, times
