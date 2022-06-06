"""
Creating combined ridership dataset.
"""
import pandas as pd
import pickle


def to_float(value):
    """
    Parameters:
        'value': input value (str, float, int, etc...)
    Returns:
        'value' as a float. Removes all commas from 'value'
        in order to cast it to a float.
    """
    if type(value) == str:
        value = value.replace(",", "")

    return float(value)


def first_four(value):
    """
    Parameters:
        'value': input value (pandas Timestamp object)
    Returns:
        First four characters of the value.
    This will be used in order to only get the year numbers
    for the data, and leave out unnecessary monthly/daily data.
    """
    value = str(value)
    return value[:4]


def make_tdf(filename, primary_col, street, region,
             secondary_region=None, secondary_col=None):
    """
    Parameters:
        'filename': CSV file relative path of bike counter data
        'primary_col': name of its total/primary bike ridership column
        'secondary_col': name of another bike ridership column, in case
            two columns need to be added together (eg. northbound and
            southbound columns). Default=None
        'street': street name
        'region': council district the bike counter is located in
        'secondary_region': secondary region bike counter is located in.
            Used for when bike counter is at boundary between two regions.
            Default=None
    Returns:
        Time-indexed DafaFrame of bike counter data, aggregated by year.
    """
    # Reading data file into time-indexed DF:
    df = pd.read_csv(filename, index_col='Date', parse_dates=True)

    # Removing all commas from number strings,
    # making all values in relevant columns floats,
    # and adding primary and secondary cols. together for total data col.:
    df[primary_col] = df[primary_col].apply(to_float)
    if secondary_col is not None:
        df[secondary_col] = df[secondary_col].apply(to_float)
        df['riders'] = df[primary_col] + df[secondary_col]
    else:
        df['riders'] = df[primary_col]

    # Cutting out unnecessary data, getting only total ridership data:
    df = df['riders']

    # Summing to annual data:
    annual = df.resample('A').sum()
    # Sorting date indices:
    annual.sort_index()

    # Reseting index to integer values, creating new date column:
    annual = annual.reset_index()

    # Adding council district, street columns:
    annual['street'] = street
    annual['council_district'] = region
    if secondary_region is not None:
        annual['secondary_council_district'] = secondary_region

    # Re-storing only year in 'Date' column:
    annual['Date'] = annual['Date'].apply(first_four)

    return annual


def main():

    # Cleaning, adding data to final_df:

    final_df = make_tdf('data\\bike_counters\\2nd_Ave.csv',
                        '2nd Ave Cycletrack', '2nd Ave', 7)

    final_df = pd.concat([
        final_df,
        make_tdf(
            'data\\bike_counters\\7th_Ave.csv',
            '2100 7th Ave Display Total', '7th Ave', 7)
    ])

    final_df = pd.concat([
        final_df,
        make_tdf(
            'data\\bike_counters\\26th_Ave.csv',
            '26th Ave SW Greenway at SW Oregon St Total',
            '26th Ave SW', 1
        )
    ])

    final_df = pd.concat([
        final_df,
        make_tdf(
            'data\\bike_counters\\39th_Ave_NE_OOS.csv',
            '39th Ave NE Greenway at NE 62nd St Total',
            '39th Ave NE', 4
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\Broadway.csv',
            'Broadway Cycle Track North Of E Union St Total',
            'Broadway', 3
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\Burke_Gilman_Trail.csv',
            'Bike North',
            'Burke-Gilman Trl', 4,
            secondary_col='Bike South'
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\Chief_Sealth_Trail.csv',
            'Bike North',
            'Chief Sealth Trl', 2,
            secondary_col='Bike South'
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\Elliott_Bay_Trail.csv',
            'Bike North',
            'Elliott Bay Trl', 7,
            secondary_col='Bike South'
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\Fremont_Bridge.csv',
            'Fremont Bridge Total',
            'Fremont Brg', 7,
            secondary_region=6
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\Mountains_To_Sound_Trail.csv',
            'Bike East',
            'Mountains to Sound Trl', 3,
            secondary_col='Bike West'
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\NW_58th_St.csv',
            'NW 58th St Greenway st 22nd Ave NW Total',
            'NW 58th St', 6
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\Spokane_St_Bridge.csv',
            'Spokane St. Bridge Total',
            'Spokane St Brg', 1,
            secondary_region=2
        )
    ])

    final_df = pd.concat([
        final_df, make_tdf(
            'data\\bike_counters\\Westlake.csv',
            'Westlake PBL and Newton St',
            'Westlake Ave N', 7
        )
    ])

    # Reseting indices of final DataFrame:
    final_df = final_df.reset_index(drop=True)

    # Saving final pandas DataFrame to file using pickle:
    with open('Data\\refined_data\\total_bike_counters.pickle', 'wb') as f:
        pickle.dump(final_df, f)
    # Saving final pandas DataFrame to CSV file:
    final_df.to_csv('Data\\refined_data\\total_bike_counters_csv.csv')


if __name__ == '__main__':
    main()
