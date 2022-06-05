import networkx as nx
import pickle


def make_graph(filename):
    """
    Creates networkx graph using bike infrastructure data from pandas
    DataFrame stored in pickle file 'filename'.
    """
    # Load bike infrastructure data:
    with open(filename) as f:
        data = pickle.load(f)

    # Put data in networkx graph:
    graph = nx.from_pandas_edgelist(
        data, 'START', 'END', edge_attr=True
    )

    return graph


def get_total_connectivity(graph):
    """
    Returns total "Connectivity Metric" for given 'graph'.
    Connectivity Metric: product of total network length (feet)
    by amount of edges for each subgraph, summed over all
    subgraphs in 'graph'. A subgraph is a cluster
    of connected nodes.

    Generally, the more disconnected a graph is (the more
    subgraphs there are), the lower the connectivity metric.
    However, if the amount of subgraphs increases as more
    subgraphs are being made, the metric rises; just not as much
    as if the bike network was being built more connected.
    """
    # Creating and counting amount of subgraphs:
    subgraphs = list(nx.connected_components(graph))
    num_subgraphs = len(subgraphs)
    # Creating total counter variable:
    total = 0
    # Iterating through all subgraphs, analyzing:
    for i in range(num_subgraphs):
        subg = graph.subgraph(subgraphs[i])
        total += subg.size(weight='SHAPE_Length') * subg.size()

    return total


def get_all_networks(filename):
    """
    Creates networkx graph from 'filename' and finds connectivity
    metric for each kind of bike infrastructure for every year,
    along with an overall network connectivity. This means six networks
    per year
    """


def main():
    pass


if __name__ == '__main__':
    main()
