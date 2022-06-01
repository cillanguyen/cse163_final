from enum import unique
import pandas as pd
# import matplotlib as plt
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt


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

    


if __name__ == "__main__":
    main()
