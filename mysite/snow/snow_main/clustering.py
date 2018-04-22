import random
import numpy as np
import math
from scipy.spatial import ConvexHull


def cluster(graph, k, distances):
    """ Find k clusters of edges in the given graph """

    vertex_clusters = _cluster_vertices(graph, k, distances)
    edges = []
    for u, l in graph.adj_list.items():
        for v, d in l:
            edges.append((u, v))
    return _group_edges(edges, vertex_clusters, distances)


def _find_mean(graph, vertices):
    X = []
    Y = []
    for v in vertices:
        x, y = graph.locations[v]
        X.append(x)
        Y.append(y)
    x_mean = sum(X)/len(vertices)
    y_mean = sum(Y)/len(vertices)

    min_d = float("inf")
    for i, vertex in enumerate(vertices):
        d = math.sqrt((X[i] - x_mean)**2 + (Y[i] - y_mean)**2)
        if d < min_d:
            min_d = d
            new_center = vertex

    return new_center


def _are_clusters_unchanged(clusters_1, clusters_2, k):

    for i in range(k):
        c1 = clusters_1[i]
        c2 = clusters_2[i]

        if c1['center'] != c2['center']:
            return False

        if len(c1['vertices']) != len(c2['vertices']):
            return False

        for v1 in c1['vertices']:
            if v1 not in c2['vertices']:
                return False

    return True


def _cluster_copy(src_clusters):
    dest_clusters = []
    for s_c in src_clusters:
        d_c = dict()
        d_c['center'] = s_c['center']
        d_c['vertices'] = []
        for v in s_c['vertices']:
            d_c['vertices'].append(v)
        dest_clusters.append(d_c)

    return dest_clusters


def _find_good_starting_centroids(graph, k, distances):
    points = []
    for v in graph.nodes:
        points.append(np.asarray(graph.locations[v]))

    points = np.asarray(points)

    hull = ConvexHull(points)

    hull_vertices = []
    for vertex in hull.vertices:
        hull_vertices.append(vertex+1)

    gap = len(hull_vertices)/k

    centers = []

    for i in range(0, len(hull_vertices), gap):
        centers.append(hull_vertices[i])

    return centers


def _cluster_vertices(graph, k, distances):
    #n = len(graph.nodes)

    centers = _find_good_starting_centroids(graph, k, distances)
    #random.sample(range(1, n), k)

    clusters = []
    for i in range(k):
        cluster_map = dict()
        cluster_map['center'] = centers[i]
        #print('Center of {}th cluster: {}'.format(i, cluster_map['center']))
        cluster_map['vertices'] = [centers[i]]
        clusters.append(cluster_map)

    loop = 0
    while loop < 50:
        new_clusters = []
        for i in range(k):
            cluster_map = dict()
            cluster_map['center'] = -1
            cluster_map['vertices'] = []
            new_clusters.append(cluster_map)

        for v in graph.nodes:
            min_dist = float('inf')
            for i in range(k):
                #print('Distance between vertices {} and {}: {}'.format(v, i, distances[v][clusters[i]['center']]))
                if distances[v][clusters[i]['center']] < min_dist:
                    min_dist = distances[v][clusters[i]['center']]
                    nearest_cluster_index = i
            new_clusters[nearest_cluster_index]['vertices'].append(v)

        for i in range(k):
            new_clusters[i]['center'] = _find_mean(graph, new_clusters[i]['vertices'])

        if _are_clusters_unchanged(clusters, new_clusters, k):
            print("Clustering has converged....")
            break

        clusters = _cluster_copy(new_clusters)
        loop = loop + 1

    return clusters


def _find_cluster_containing_vertex(vertex, clusters):
    for i, c in enumerate(clusters):
        if vertex in c['vertices']:
            return i
    return 0


def _group_edges(edges, vertex_clusters, distances):
    clusters = []
    for i in range(len(vertex_clusters)):
        clusters.append([])

    covered = set()
    for u, v in edges:
        if (u, v) in covered or (v, u) in covered:
            continue
        c_u_index = _find_cluster_containing_vertex(u, vertex_clusters)
        c_v_index = _find_cluster_containing_vertex(v, vertex_clusters)

        if c_u_index != c_v_index:
            cost_u = abs(distances[u][vertex_clusters[c_u_index]['center']] -
                         distances[u][vertex_clusters[c_v_index]['center']])
            cost_v = abs(distances[v][vertex_clusters[c_v_index]['center']] -
                         distances[v][vertex_clusters[c_u_index]['center']])

            if cost_u < cost_v:
                index = c_u_index
            else:
                index = c_v_index
        else:
            index = c_u_index

        clusters[index].append((u, v))
        covered.add((u, v))

    return clusters
