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

    # get the years in the dataset (timespan assigment edsteam)

    existing_file = pd.read_csv('Existing_Bike_Facilities.csv')
    existing_file = existing_file[['UNITDESC', 'CATEGORY', 'INSTALL_DATE',
                                   'SHAPE_Length', 'PRIMARYDISTRICTCD',
                                   'SECONDARYDISTRICTCD']]

    # make a function to spilt the string from ()
    # use append to append to the entire dataframe


    # making a graph for each year with the different bike infrastructure

    # plan_file = gpd.read_file('/Data/Planned_Bike_Facilities/Planned_Bike_Facilities.shp')

    # fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))




if __name__ == "__main__":
    main()
