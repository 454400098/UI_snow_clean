import heapq
import network


def find(graph, s, t):
    """ Find shortest distance and path between two given nodes """

    h = []
    dist = {}
    prev = {}
    for v in graph.adj_list.keys():
        dist[v] = 99999
        prev[v] = -1

    dist[s] = 0

    h.append((dist[s], s))
    heapq.heapify(h)

    while len(h) > 0:
        d1, u = heapq.heappop(h)
        if u == t:
            break
        for v, d in graph.adj_list[u]:
            if (dist[u] + d) < dist[v]:
                if (dist[v], v) in h:
                    h.remove((dist[v], v))
                dist[v] = dist[u] + d
                prev[v] = u
                heapq.heappush(h, (dist[v], v))

    path = [t]
    n = t
    while n != s:
        path.insert(0, prev[n])
        n = prev[n]

    return dist[t], path


if __name__ == '__main__':

    g = network.Graph()
    test_graph = network.CPGraph(g)
    test_graph.adj_list = {
        130: [(55, 94), (111, 39)],
        3: [(5, 150), (122, 277), (47, 269)],
        132: [(16, 182), (118, 131), (123, 29)],
        5: [(3, 150), (37, 120), (122, 128)],
        9: [(10, 80)],
        10: [(9, 80), (22, 49), (33, 70), (39, 31), (36, 76)],
        16: [(132, 182), (40, 31), (62, 53), (38, 35)],
        21: [(25, 38), (39, 24), (33, 56)],
        22: [(10, 49), (80, 18), (125, 21)],
        25: [(21, 38), (126, 4), (39, 36)],
        30: [(119, 61), (120, 63), (35, 114)],
        31: [(67, 202), (37, 414), (114, 585)],
        33: [(10, 70), (21, 56), (37, 24)],
        35: [(30, 114)],
        36: [(10, 76)],
        37: [(5, 120), (31, 414), (33, 24)],
        38: [(16, 35), (40, 26), (66, 128)],
        39: [(10, 31), (21, 24), (25, 36)],
        40: [(16, 31), (38, 26), (118, 448)],
        44: [(54, 258), (67, 32)],
        47: [(3, 269), (72, 62)],
        54: [(44, 258)],
        55: [(130, 94)],
        61: [(80, 15)],
        62: [(16, 53), (119, 15), (66, 155), (88, 15)],
        66: [(38, 128), (62, 155), (67, 112)],
        67: [(31, 202), (44, 32), (66, 112)],
        72: [(47, 62), (87, 237), (88, 354)],
        80: [(22, 18), (61, 15)],
        81: [(102, 42)],
        83: [(94, 84), (111, 12)],
        86: [(102, 167)],
        87: [(72, 237)],
        88: [(62, 15), (72, 354), (90, 71), (119, 11)],
        90: [(88, 71), (94, 59), (120, 18)],
        94: [(83, 84), (90, 59)],
        102: [(81, 42), (86, 167), (117, 120)],
        111: [(83, 12), (130, 39)],
        114: [(31, 585)],
        117: [(102, 120), (118, 119)],
        118: [(40, 448), (117, 119), (132, 131)],
        119: [(30, 61), (62, 15), (88, 11), (120, 45)],
        120: [(30, 63), (90, 18), (119, 45)],
        122: [(3, 277), (5, 128)],
        123: [(132, 29)],
        125: [(22, 21)],
        126: [(25, 4)]
    }

    print(find(test_graph, 132, 10))