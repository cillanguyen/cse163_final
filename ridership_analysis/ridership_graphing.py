"""
Plots the amount of riders at various bike counters across Seattle
per year using cleaned ridership data.
"""
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np


def conform_data(filename):
    """
    Parameters:
        'filename': file name of pickle file with pandas DataFrame with
        bike ridership info for Seattle bike counters by year.
    Returns:
        Reorganized DataFrame, with streets as columns along with a
        "total" ridership column, representing bike counters with significant
        amount of data available (no more than three missing rows in input
        data). Values are the percent change in riders each year (first year
        is 0).
    """

    # Opening data file:
    with open(filename, 'rb') as f:
        all_data = pickle.load(f)

    # Reordering column/row data to be more suitable for plotting:
    data = all_data.pivot(index='Date', columns='street', values='riders')

    # Making all dates integers:
    data.reset_index(inplace=True)
    data['Date'] = data['Date'].apply(lambda s: int(s))
    data.set_index('Date', inplace=True)

    # Replacing 0's with NaN:
    data.replace(0, np.nan, inplace=True)
    # If column has more than three NaN rows, removed:
    columns = data.columns
    for col in columns:
        if data[col].isna().sum() > 3:
            data.drop(col, inplace=True, axis=1)

    # Making totals column:
    data['Total'] = data.sum(axis=1, skipna=False)
    print(data)

    first_year = data.index[0]

    # Percent Change DF for columns with enough data available:
    per_chg_data = pd.DataFrame(index=data.index)

    # Removing columns with more than 3 "NaN" rows,
    # making percent change cols., adding to new DF:
    years = data.index
    new_columns = data.columns

    for col in new_columns:
        for year in years:
            if year == first_year:
                per_chg_data.loc[year, col] = np.nan
            else:
                pres = data.loc[year, col]
                prev = data.loc[year - 1, col]
                per_chg_data.loc[year, col] = 100 * (pres - prev) / prev
    # Editing-out strange outliers in data:
    per_chg_data.loc[2013, 'Fremont Brg'] = np.nan
    per_chg_data.loc[2014, 'Mountains to Sound Trl'] = np.nan

    return per_chg_data


def plot_data(data):
    """
    Parameters:
        'data': pandas DataFrame with re-organized data on yearly
        bike ridership.
    Returns:
        Plot of bike ridership over time (yearly) at different bike
        counters in Seattle, along with a plot of the overall bike
        ridership figures over time.
    """
    fig, [ax1, ax2] = plt.subplots(2, sharex=True)

    # Plotting each column in re-organized data:
    streets = ['26th Ave SW', '2nd Ave', 'Broadway', 'Burke-Gilman Trl',
               'Elliott Bay Trl', 'Fremont Brg', 'Mountains to Sound Trl',
               'NW 58th St', 'Spokane St Brg']
    data.plot(y=streets, ax=ax1, legend=True, figsize=(10, 10))
    data.plot(y='Total', ax=ax2, figsize=(10, 10))
    ax1.set_ylabel('Individual Percent Change')
    ax2.set_ylabel('Total Percent Change')
    ax1.set_title('Annual Percent Change in Bike Ridership')
    ax1.axhline(y=0, color='black', linewidth=1)
    ax2.axhline(y=0, color='black', linewidth=1)

    plt.savefig('ridership_analysis\\annual_ridership.png')


def main():

    reorganized_data = conform_data('Data\\refined_data\\' +
                                    'total_bike_counters.pickle')
    print(reorganized_data)
    # Plotting data:
    plot_data(reorganized_data)


if __name__ == '__main__':
    main()
