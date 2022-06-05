import pandas as pd
import pickle


def clean_data(filename):
    """
    Parameters:
        'filename': name of CSV data file of existing bike
        infrastructure data.
    Returns:
        Filtered dataframe with existing bike infrastructre data.
    """
    # Opening file, loading to dataframe:
    df = pd.read_csv(filename, parse_dates=True)

    # Getting only necessary columns:
    df = df[['UNITDESC', 'CATEGORY', 'INSTALL_DATE',
             'PRIMARYDISTRICTCD', 'SECONDARYDISTRICTCD',
             'SHAPE_Length']]

    # Dropping rows with missing data (unusable):
    no_street = df['UNITDESC'].notnull()
    no_category = df['CATEGORY'].notnull()
    no_date = df['INSTALL_DATE'].notnull()
    no_length = df['SHAPE_Length'].notnull()

    df = df[no_street & no_category & no_date & no_length]
    # Re-indexing:
    df.reset_index(drop=True, inplace=True)

    # Recording dates as only the years;
    # (For some reason, the dates are already given as strings
    # and not Timestamp objects):
    df['INSTALL_DATE'] = df['INSTALL_DATE'].apply(lambda ts: int(ts[:4]))

    # Removing things in parentheses in 'UNITDESC' column:
    df['UNITDESC'] = df['UNITDESC'].apply(lambda s: s.split(' (')[0])

    return df


def start(s):
    """
    Returns name of starting intersection of bike infrastructure segment,
    given string 's'. Street names sorted alphanumerically.
    """
    split_str = s.split(' BETWEEN ')
    street = split_str[0]
    intersectors = split_str[1]
    start_street = intersectors.split(' AND ')[0]
    name_list = sorted([street, start_street])

    return name_list[0] + ' AND ' + name_list[1]


def end(s):
    """
    Returns name of ending intersection of bike infrastructure segment,
    given string 's'. Street names sorted alphanumerically.
    """
    split_str = s.split(' BETWEEN ')
    street = split_str[0]
    intersectors = split_str[1]
    end_street = intersectors.split(' AND ')[1]
    name_list = sorted([street, end_street])

    return name_list[0] + ' AND ' + name_list[1]


def main():

    path = 'Data\\existing_bike_facilities\\Existing_Bike_Facilities.csv'
    bike_data = clean_data(path)

    bike_data['STREET'] = bike_data['UNITDESC'].apply(
        lambda s: s.split('BETWEEN')[0]
    )
    bike_data['START'] = bike_data['UNITDESC'].apply(start)
    bike_data['END'] = bike_data['UNITDESC'].apply(end)

    bike_data = bike_data[['CATEGORY', 'INSTALL_DATE', 'PRIMARYDISTRICTCD',
                           'SECONDARYDISTRICTCD', 'SHAPE_Length',
                           'STREET', 'START', 'END']]

    with open('Data\\refined_data\\existing_facilities_data.pickle',
              'wb') as f:
        pickle.dump(bike_data, f)
    bike_data.to_csv('Data\\refined_data\\existing_facilities_data_csv.csv')


if __name__ == '__main__':
    main()
