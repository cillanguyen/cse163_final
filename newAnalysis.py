import pandas as pd
import geopandas as gpd
import seaborn as sns
# from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt


def main():

    # ploting a line graph for num of infrastructure each year 2014-2020

    # read the data and filter based on year
    df = pd.read_csv('Existing_Bike_Facilities.csv', index_col='INSTALL_DATE',
                     parse_dates=True)
    num_rows = len(df.index)
    count = [1]*num_rows
    df['NUM'] = count
    df = df[['CATEGORY', 'PRIMARYDISTRICTCD', 'NUM', 'UNITDESC',
             'SECONDARYDISTRICTCD', 'SHAPE_Length']]

    # use groupby to keep track of the number of bike infrastructures
    year = df.groupby([df.index.year, 'CATEGORY']).sum()
    year = year.loc[2010.0: 2020.0]
    sns.lineplot(data=year, x='INSTALL_DATE', y='NUM', hue='CATEGORY')

# make plot line smoother (need to uncomment scipy.interpolate)
    # line_plot = make_interp_spline('INSTALL_DATE', 'NUM')
    # num_plot = line_plot(install_plot)
    # plt.plot(install_plot, num_plot)

    plt.xlabel('Dates of Installment')
    plt.ylabel('Num of Bike Infrastructures')
    plt.title('Number of Bike Infrastructures 2010-2020')
    # plt.show()
    plt.savefig('bike_infrastructures_plot.png')

    # map the bike infractures

    planned_file = gpd.read_file('Data/Planned_Bike_Facilities/Planned_Bike_Facilities.shp')
    print(planned_file.columns)
    # planned_file.plot()

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))
    map_2010 = planned_file.loc[2010.0]
    map_2010.plot(column='Category', legend=True, ax=ax1)
    ax1.set_title('2010 infrastructures')

    map_2012 = planned_file.loc[2012.0]
    map_2012.plot(column='Category', legend=True, ax=ax2)
    ax2.set_title('2012 infrastructures')

    map_2014 = planned_file.loc[2014.0]
    map_2014.plot(column='Category', legend=True, ax=ax3)
    ax3.set_title('2014 infrastructures')

    map_2020 = planned_file.loc[2020.0]
    map_2020.plot(column='Category', legend=True, ax=ax4)
    ax4.set_title('2020 infrastructures')
    plt.savefig('bike_infrastructures_map.png')


if __name__ == "__main__":
    main()
