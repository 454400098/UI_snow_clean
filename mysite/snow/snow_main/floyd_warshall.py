def find_distances(graph):
    """ Find all pair shortest distances via Floyd Warshall Algorithm """

    n = len(graph.nodes)
    dist = []
    for i in range(n+1):
        d_temp = []
        p_temp = []
        for j in range(n+1):
            d_temp.append(99999999)
            p_temp.append([])
        dist.append(d_temp)

    for i in range(n + 1):
        dist[i][i] = 0

    for u, l in graph.adj_list.items():
        for v, d in l:
            dist[u][v] = d

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
