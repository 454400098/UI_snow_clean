import osmnx as ox
import argparse
import network, dijkstra
from tour_planner import TourPlanner
from PIL import Image

def snow_clearance(k,place,pp1,pp2):
    
    #place = "Rutgers University"
    #k = int(args["k"])
    pp_vertices = pp1, pp2

    G = ox.graph_from_address(place, network_type='drive')

    graph = network.convert_osnx_to_own(G)

    c, priority_path = dijkstra.find(graph, pp_vertices[0], pp_vertices[1])
    print('Priority path for snow clearance: {}'.format(priority_path))

    priority_edges = []
    for i in range(0, (len(priority_path)-1)):
        priority_edges.append((graph.val_node_map[priority_path[i]], graph.val_node_map[priority_path[i + 1]]))
        priority_edges.append((graph.val_node_map[priority_path[i + 1]], graph.val_node_map[priority_path[i]]))

    ec = ['y' if e in priority_edges else 'none' for e in G.edges()]

    ox.plot_graph(G, node_size=0, edge_color=ec,save=True, show=False, filename='priority_path')

    tour_planner = TourPlanner(graph=graph, k=k)

    print("\n\n##################################################\n")
    print('Finding clusters on the map based on road connectivity\n')
    print("##################################################\n")

    clusters = tour_planner.cluster()
    m_clusters = []
    for cluster in clusters:
        m_cluster = []
        for u, v in cluster:
            m_cluster.append((graph.val_node_map[u], graph.val_node_map[v]))
        m_clusters.append(m_cluster)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k' ]
    ec = []
    for (u, v) in G.edges():
        for i, m_cluster in enumerate(m_clusters):
            if (u, v) in m_cluster or (v, u) in m_cluster:
                ec.append(colors[i])
                break
    ox.plot_graph(G, node_size=0, edge_color=ec,save=True, show=False, filename='clustering')

    print("\n\n##################################################\n")
    print('Planning routes for all the vehicles\n')
    print("##################################################\n")

    tours, times = tour_planner.plan(clusters, priority_path)

    for i, tour in enumerate(tours):
        print('\n\n######### VEHICLE {} ########\n\nRoute: {} \n\nTime: {}'.format(i, tours[i], times[i]))
    display=''
    for i, tour in enumerate(tours):
        display=display+'\n\n######### VEHICLE {} ########\n\nRoute: {} \n\nTime: {}'.format(i, tours[i], times[i])
    print (display)

    tour_clusters = []
    for tour in tours.values():
        tour_cluster = []
        for i in range(len(tour)-1):
            tour_cluster.append((graph.val_node_map[tour[i]], graph.val_node_map[tour[i+1]]))
        tour_clusters.append(tour_cluster)

    ec = []
    for (u, v) in G.edges():
        flag = False
        for i, tour_cluster in enumerate(tour_clusters):
            if (u, v) in tour_cluster or (v, u) in tour_cluster:
                ec.append(colors[i])
                flag = True
                break
        if not flag:
            ec.append(colors[-1])

    ox.plot_graph(G, node_size=0, edge_color=ec,save=True, show=False, filename='end')

    print("Done planning!")
    img = Image.open('images/priority_path.png')
    img.show('aaa')
    img = Image.open('images/end.png')
    img.show('bbb')
    return display





