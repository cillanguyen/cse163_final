import pandas as pd
# import matplotlib as plt
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
# import seaborn as sn

# change question a to...
    # how many different bike infrastructure in seattle during different years?
    # line graph and geospecial data to visual (different year to view bike
    # infrastructures)
    # making plot
        # sort by date 2014-2020
        # filter by ",,,,,,,"
        # make new dataframe with specific columns

# question b:
    # combine the bike counters that represent different regions
    # using the regions to look at the exisiting dataset
    # use time series (choose year and add all of the bikes riding)

# question c:
    # machine learning


def main():

    # ploting a line graph for the num of infrastructure for each year 2014-2020

    existing_file = pd.read_csv('Existing_Bike_Facilities.csv')
    df_file = existing_file.replace(",", "")
    df_file = existing_file[(existing_file['CATEGORY'] == 'BKF-SHW') |
                            (existing_file['CATEGORY'] == 'BKF-NGW')]
    df_file = df_file[(df_file['INSTALL_DATE'] >= '2014') &
                      (df_file['INSTALL_DATE'] <= '2020')]
    # plot is NOT running
    sns.relplot(data=df_file, x='INSTALL_DATE', y='CATEGORY', kind='line')

    # making a graph for each year with the different bike infrastructure

    plan_file = gpd.read_file('/Data/Planned_Bike_Facilities/Planned_Bike_Facilities.shp')

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))
    



if __name__ == "__main__":
    main()
