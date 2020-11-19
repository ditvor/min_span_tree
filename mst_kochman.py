import networkx as nx
import matplotlib.pyplot as plt
import math
from itertools import product
import random


def min_span_tree(points_dict, visual=True):
    """ Find a minimum spanning tree for a graph.
    Return an adjacency list.
    Creates a visualization of the graph if visual=True (default=True).

    """
    g = nx.Graph()

    # add nodes from an input dict as keys
    g.add_nodes_from(points_dict.keys())

    # add node coordinates from input dict
    for node, coordinates in points_dict.items():
        g.nodes[node]['pos'] = coordinates

    # creating an edge list that consists of pair of nodes with a distance as a weight (node_1, node_2, distance)
    edge_list = list((a, b, round(math.dist(points_dict[a], points_dict[b]), 1))
                     for a, b in product(range(1, len(points_dict)+1), range(1, len(points_dict)+1))
                     if a != b)

    # adding edges to the graph
    g.add_weighted_edges_from(edge_list)

    # apply networkx package to determine the minimum spanning tree
    mst = nx.minimum_spanning_tree(g)

    if visual:
        visualize_graph(mst)
    return mst.edges()


def visualize_graph(graph):
    """ Creates visualization for the graph"""

    ax = plt.subplot()

    node_pos = nx.get_node_attributes(graph, 'pos')
    edge_weight = nx.get_edge_attributes(graph, 'weight')

    node_col = ['white']

    # drawing the nodes
    nx.draw_networkx_nodes(graph, node_pos, node_color=node_col, node_size=450, edgecolors='black', ax=ax)

    # drawing the nodes labels
    nx.draw_networkx_labels(graph, node_pos)

    # drawing the edges if paths=True (shows all the connections)

    nx.draw_networkx_edges(graph, node_pos, edge_color='red', style='solid', width=2)

    # drawing the edge labels
    # nx.draw_networkx_edge_labels(graph, node_pos, edge_labels=edge_weight)

    plt.title('Minimum spanning tree for the graph')
    ax.set_axis_on()
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.show()


if __name__ == '__main__':
    test_points = {i: (random.random() * 100.0, random.random() * 100.0) for i in range(1, 10)}

    print(min_span_tree(test_points, visual=True))
