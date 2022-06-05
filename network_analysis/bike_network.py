import networkx as nx
import pandas as pd
import pickle


def make_graph(data):
    """
    Creates networkx graph using bike infrastructure data from pandas
    DataFrame 'data'.
    """
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


def get_all_networks():
    """
    Creates networkx graphs from bike infrastructure data and finds
    connectivity metric for each kind of bike infrastructure for every year,
    along with an overall network connectivity. This means six networks
    per year, one for Bike Lanes (BL), Protected Bike Lanes (PBL),
    Neighborhood Greenways (NGW), Sharrows (SHW), Off-Street Paths
    (OFFST), and the overall bike network.

    Dates start with 2012, since that is the earliest year with
    available bike ridership data from any of the bike counters.
    """
    # Making pandas DataFrame to track connectivity of each kind and overall
    # network connectivity by year:
    connectivity = pd.DataFrame(index=[y for y in range(2012, 2022)])

    existing_inf = pd.read_csv(
        'Data\\refined_data\\existing_facilities_data_csv.csv'
    )

    # Going by each year that has available ridership data:
    for year in range(2012, 2022):
        # Defining past years to be included for each yearly iteration:
        present_data = existing_inf[existing_inf['INSTALL_DATE'] <= year]

        # Analyzing overall present network for this year:
        connectivity.loc[year, 'Overall'] = get_total_connectivity(
            make_graph(present_data)
        )

        # Analyzing each infrastructure type for this year:
        for inf_type in ['BKF-BL', 'BKF-PBL', 'BKF-NGW', 'BKF-SHW',
                         'BKF-OFFST']:
            # Applying a mask to only get desired infrastructure
            # type for the year:
            inf_data = present_data[present_data['CATEGORY'] == inf_type]
            # Making, analyzing specific infrastructure network:
            connectivity.loc[year, inf_type] = get_total_connectivity(
                make_graph(inf_data)
            )

    # Saving connectivity DataFrame as pickle file:
    with open('network_analysis\\connectivity.pickle', 'wb') as f2:
        pickle.dump(connectivity, f2)
    # Saving connectivity DataFrame as CSV:
    connectivity.to_csv('network_analysis\\connectivity_csv.csv')


def main():
    get_all_networks()


if __name__ == '__main__':
    main()
