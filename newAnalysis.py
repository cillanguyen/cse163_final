from enum import unique
import pandas as pd
# import matplotlib as plt
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt


def main():

    # ploting a line graph for the num of infrastructure for each year 2014-2020

    df = pd.read_csv('Existing_Bike_Facilities.csv', index_col='INSTALL_DATE', parse_dates=True)
    num_rows = len(df.index)
    count = [1]*num_rows
    df['NUM'] = count
    df = df[['CATEGORY','PRIMARYDISTRICTCD', 'NUM']]
    
    year = df.groupby([df.index.year, 'CATEGORY']).sum()
    print(year)

    # filter the data within the year between 2014 to 2022

    


if __name__ == "__main__":
    main()
