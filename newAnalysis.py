import pandas as pd
import geopandas as gpd
import seaborn as sns
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
    year = df.groupby([df.index.year, 'CATEGORY']).sum()
    year = year.loc[2010.0: 2021.0]

    sns.lineplot(data=year, x='INSTALL_DATE', y='NUM', hue='CATEGORY')

    plt.xlabel('Dates of Installment')
    plt.ylabel('Segments of Bike Infrastructures')
    plt.title('Number of Bike Infrastructures built in 2010-2021')
    plt.savefig('bike_infrastructures_plot.png')

    # map the bike infractures

    planned_file = gpd.read_file(
        'Data/existing_bike_facilities/Existing_Bike_Facilities.shp')

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))

    # plot 2010
    data_2010 = planned_file[planned_file['INSTALL_DA'] == '2010-12-31']
    planned_file.plot(color='#EEEEEE', ax=ax1)
    data_2010.plot(column='CATEGORY', legend=True, ax=ax1)
    ax1.set_title('Bike Infrastructures built in 2010')

    # plot 2014
    data_2014 = planned_file[planned_file['INSTALL_DA'] == '2014-12-31']
    data_2014 = planned_file[planned_file['INSTALL_DA'] == '2013-12-31']
    data_2014 = planned_file[planned_file['INSTALL_DA'] == '2012-12-31']
    planned_file.plot(color='#EEEEEE', ax=ax2)
    data_2014.plot(column='CATEGORY', legend=True, ax=ax2)
    ax2.set_title('Bike Infrastructures built in 2012-2014')

    # plot 2018
    data_2018 = planned_file[planned_file['INSTALL_DA'] == '2018-12-31']
    data_2018 = planned_file[planned_file['INSTALL_DA'] == '2017-12-31']
    data_2018 = planned_file[planned_file['INSTALL_DA'] == '2016-12-31']
    data_2018 = planned_file[planned_file['INSTALL_DA'] == '2015-12-31']
    planned_file.plot(color='#EEEEEE', ax=ax3)
    data_2018.plot(column='CATEGORY', legend=True, ax=ax3)
    ax3.set_title('Bike Infrastructures built in 2015-2018')

    # plot 2021
    data_2021 = planned_file[planned_file['INSTALL_DA'] == '2021-12-31']
    data_2021 = planned_file[planned_file['INSTALL_DA'] == '2020-12-31']
    data_2021 = planned_file[planned_file['INSTALL_DA'] == '2019-12-31']
    data_2021 = planned_file[planned_file['INSTALL_DA'] == '2018-12-31']
    planned_file.plot(color='#EEEEEE', ax=ax4)
    data_2021.plot(column='CATEGORY', legend=True, ax=ax4)
    ax4.set_title('Bike Infrastructures built in 2018-2021')

    plt.savefig('bike_infrastructures_map.png')


if __name__ == "__main__":
    main()
