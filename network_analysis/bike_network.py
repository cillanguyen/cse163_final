import networkx as nx
import pandas as pd
import pickle
import matplotlib.pyplot as plt


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
    along with percent change per year. This means six networks
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
            connectivity.loc[year, inf_type] = \
                get_total_connectivity(make_graph(inf_data))

    # Saving connectivity DataFrame as pickle file:
    with open('network_analysis\\connectivity.pickle', 'wb') as f2:
        pickle.dump(connectivity, f2)
    # Saving connectivity DataFrame as CSV:
    connectivity.to_csv('network_analysis\\connectivity_csv.csv')

    return connectivity


def plot_connectivity(data):
    """
    Plots connectivity for all bike infrastructure types and overall
    bike network over time, given connectivity DataFrame 'data'.
    """
    fig, ax = plt.subplots(1)

    for col in ['Overall Network', 'Unprotected Bike Lanes',
                'Protected Bike Lanes', 'Neighborhood Greenways',
                'Sharrows', 'Off-Street Trails']:
        data.plot(use_index=True, y=col, ax=ax, legend=True)
    plt.xlabel('Year')
    plt.ylabel('Connectivity Percent Change')
    plt.title('Bike Network Connectivity Annual Percent Change')

    plt.savefig('network_analysis\\connectivity_graph.png')


def calc_percent_change(data):
    """
    Creates yearly percent change columns for each kind of bike infrastructure
    in pandas DataFrame 'data', with first entries as 0.
    """
    columns = data.columns

    for year in range(2012, 2022):
        for col in columns:
            # Renaming columns:
            if col == 'Overall':
                new_col = 'Overall Network'
            elif col == 'BKF-BL':
                new_col = 'Unprotected Bike Lanes'
            elif col == 'BKF-PBL':
                new_col = 'Protected Bike Lanes'
            elif col == 'BKF-NGW':
                new_col = 'Neighborhood Greenways'
            elif col == 'BKF-SHW':
                new_col = 'Sharrows'
            elif col == 'BKF-OFFST':
                new_col = 'Off-Street Trails'

            # Since there is no data before 2012:
            if year == 2012:
                data.loc[year, new_col] = 0
            # Calc. percent change for each infrastructure type, each year:
            else:
                prev = data.loc[year - 1, col]
                pres = data.loc[year, col]
                data.loc[year, new_col] = 100 * (pres - prev) / prev
    data.to_csv('network_analysis\\connectivity_csv.csv')

    return data


def main():
    data = get_all_networks()
    data = calc_percent_change(data)
    plot_connectivity(data)


if __name__ == '__main__':
    main()
