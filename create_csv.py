import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import os


def create_csv(df, district):
    """
    A function that creates a new csv file only contains the data
    about the 'year', 'district', and 'category' in each region.
    """
    df = df[df['PRIMARYDISTRICTCD'] == district]
    year = df.groupby([df.index.year, 'CATEGORY', 'PRIMARYDISTRICTCD']).sum()
    filename = district + '.csv'
    dir_path = 'DISTRICT'
    path = os.path.join(dir_path, filename)
    year.to_csv(path)


def main():
    """
    A function that used to set the counts for different bike infrastructure
    and call create_csv function for creating new csv files related to the
    number of different bike infrastructures in each districts.
    """
    df = pd.read_csv('Existing_Bike_Facilities.csv', index_col='INSTALL_DATE',
                     parse_dates=True)
    num_rows = len(df.index)
    count = [1]*num_rows
    df['NUM'] = count
    df = df[['CATEGORY', 'PRIMARYDISTRICTCD']]
    create_csv(df, 'DISTRICT1')
    create_csv(df, 'DISTRICT2')
    create_csv(df, 'DISTRICT3')
    create_csv(df, 'DISTRICT4')
    create_csv(df, 'DISTRICT5')
    create_csv(df, 'DISTRICT6')
    create_csv(df, 'DISTRICT7')
    # make plots for the existing_bike_facilities.shp based
    # on the different districts.
    path = 'Data/existing_bike_facilities/Existing_Bike_Facilities.shp'
    df = gpd.read_file(path)
    df.plot(column='PRIMARYDIS', legend=True)
    plt.savefig('Seattle.png')


if __name__ == "__main__":
    main()
