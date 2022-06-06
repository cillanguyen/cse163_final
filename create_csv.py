from enum import unique
from matplotlib.transforms import Bbox
import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle


def create_csv(df, district):
    df = df[df['PRIMARYDISTRICTCD'] == district]
    year = df.groupby([df.index.year, 'CATEGORY', 'PRIMARYDISTRICTCD']).sum()
    filename = district + '.csv'
    year.to_csv(filename)

def main():

    # ploting a line graph for the num of infrastructure for each year 2014-2020

    df = pd.read_csv('Existing_Bike_Facilities.csv', index_col='INSTALL_DATE', parse_dates=True)
    num_rows = len(df.index)
    count = [1]*num_rows
    df['NUM'] = count
    df = df[['CATEGORY','PRIMARYDISTRICTCD']]
    
    # create_csv(df, 'DISTRICT1')
    # create_csv(df, 'DISTRICT2')
    # create_csv(df, 'DISTRICT3')
    # create_csv(df, 'DISTRICT4')
    # create_csv(df, 'DISTRICT5')
    # create_csv(df, 'DISTRICT6')
    # create_csv(df, 'DISTRICT7')

    # filter the data within the year between 2014 to 2022
 


    # with open('Data/refined_data/existing_facilities_data.pickle', 'rb') as f:
    #     df = pickle.load(f)
    #     # print(df.columns)
    #     df = df[['CATEGORY', 'INSTALL_DATE', 'PRIMARYDISTRICTCD','SHAPE_Length']]
    #     mask1 = df['PRIMARYDISTRICTCD']=='DISTRICT2'
    #     mask2 = df['INSTALL_DATE'] == '2015'
    #     data = df[mask1 & mask2]
    #     # print(data)
    #     print(data)

    # with open('Data/refined_data/total_bike_counters.pickle', 'rb') as f:
    #     df = pickle.load(f)
    #     data = df[df['council_district']==2]
    #     print(data)
    # visualize the geospaial data
    df = gpd.read_file('Data/existing_bike_facilities/Existing_Bike_Facilities.shp')
    # print(df.columns)
    df.plot(column='PRIMARYDIS', legend=True)
    plt.savefig('Seattle.png')

    


if __name__ == "__main__":
    main()
