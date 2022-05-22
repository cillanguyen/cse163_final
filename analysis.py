import pandas as pd
# import matplotlib as plt
# import seaborn as sn

# change question a to...
    # how many different bike infrastructure in seattle during different years?
    # line graph and geospecial data to visual (different year to view bike
    # infrastructures)

# question b:
    # combine the bike counters that represent different regions
    # using the regions to look at the exisiting dataset
    # use time series (choose year and add all of the bikes riding)

# question c:
    # machine learning


def main():
    existing_file = pd.read_csv('Existing_Bike_Facilities.csv')
    print(existing_file.head())


if __name__ == "__main__":
    main()
