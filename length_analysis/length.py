"""
Analyzes and plots the total length of the bike infrastructure network
over time.
"""
import pandas as pd
import matplotlib.pyplot as plt


def get_length(filename):
    """
    Parameters:
        'filename': name of data file with bike infrastructure data.
    Returns:
        Pandas Series with total length of the bike network (mi.) as values,
        and indices as years. All data before 2012 is added to 2012.
    """

    data = pd.read_csv('Data\\refined_data\\existing_facilities_data_csv.csv')

    data = pd.DataFrame(data.groupby('INSTALL_DATE')['SHAPE_Length'].sum())
    data.reset_index(inplace=True)

    # Adding all pre-2012 data to 2012:
    is_before_or_2012 = data['INSTALL_DATE'] <= 2012
    before = data[is_before_or_2012]

    data['INSTALL_DATE'] = data['INSTALL_DATE'].apply(lambda s: int(s))
    data.loc[9] = before.sum()
    data = data[data['INSTALL_DATE'] >= 2012]
    data.loc[9, 'INSTALL_DATE'] = 2012
    data = data.reset_index(drop=True)

    # Making length a running sum over the years; changing to miles from feet:
    data['Total Length'] = data['SHAPE_Length'].cumsum() / 5280

    return data


def plot_length(data):
    """
    Parameters:
        'data': pandas Series of total bike infrastructure length over
        time, with indices as years.
    Returns:
        Plot of total length of the network (mi.) over time, from 2012
        to 2022. Saves figure.
    """
    data.plot(x='INSTALL_DATE', y='Total Length', legend=False)
    plt.title('Total Bike Network Length Over Time')
    plt.xlabel('Year')
    plt.ylabel('Total Network Length (mi.)')

    plt.savefig('length_analysis\\length_plot.png')


def main():

    lengths = get_length('Data\\refined_data\\' +
                         'existing_facilities_data_csv.csv')
    plot_length(lengths)


if __name__ == '__main__':
    main()
