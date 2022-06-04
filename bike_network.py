import networkx as nx
import pickle
import math


def make_graph(data):
    """
    Creates networkx graph using information from pandas DataFrame 'data'.
    """
    with open('Data\\refined_data\\existing_facilities_data.pickle',
              'rb') as f:
        data = pickle.load(f)

    graph = nx.from_pandas_edgelist(
        data, 'START', 'END', edge_attr=True
    )

    return graph


def get_total_connectivity(graph):
    """
    Returns total connectivity of a graph's disconnected subgraphs.
    Connectivity score of each subgraph: product of total amount of edges,
    total length of network in feet, and average node connectivity.
    Sum for all subgraphs, and divide by the amount of subgraphs.
    A subgraph is a cluster of connected nodes.
    """
    # Creating subgraphs:
    subgphs = list(nx.connected_components(graph))
    num_subgphs = len(subgphs)
    # Creating total variable:
    total = 0
    # Iterating through all subgraphs, analyzing:
    for i in range(num_subgphs):
        subg = graph.subgraph(subgphs[i])
        avg = nx.average_node_connectivity
        total += avg * subg.size(weight='SHAPE_Length') * subg.size()

    return total


def main():

    with open('Data\\refined_data\\existing_facilities_data.pickle',
              'rb') as file:
        data = pickle.load(file)

    # Creating bike network graph with networkx:
    bike_graph = make_graph(data)
    # Computing total length of bike infrastructure network:
    length = bike_graph['SHAPE_Length'].sum()

    return connected_coeff(bike_graph, length)


if __name__ == '__main__':
    main()
