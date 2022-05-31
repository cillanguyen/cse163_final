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
    df = pd.read_csv(filename)

    # Getting only necessary columns:
    df = df[['UNITDESC', 'CATEGORY', 'INSTALL_DATE',
             'PRIMARYDISTRICTCD', 'SECONDARYDISTRICTCD',
             'SHAPE_Length']]

    # Dropping rows with no street name, category or install date:
    is_na = df[['UNITDESC', 'CATEGORY', 'INSTALL_DATE', 'SHAPE_Length']].isnull()
    df

    # Remaking date column as strings of year numbers:
    df['INSTALL_DATE'] = df['INSTALL_DATE'].apply(lambda ts: str(ts.year))

    return df


def main():

    bike_data = clean_data('Data\\existing_bike_facilities\\' +
                           'Existing_Bike_Facilities.csv')
    print(bike_data.head())
    # with open('Data\\refined_data\\existing_facilities_data.pickle',
    #           'wb') as f:
        pickle.dump(bike_data, f)


if __name__ == '__main__':
    main()
