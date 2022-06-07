from locale import normalize
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np
import os

# 1. define a function
# 2. call function 7 time 
# 3. print the result each time

def make_feature(name_dict, test, num):
    """
    This function used to do machine learning on the current dataset
    and obtain the feature importance for the regressor model which 
    represent the influence on the number of riders
    by different bike infrastructure.
    The feature influences for each distrcit would be showed as a bar plot.
    """
    df = pd.DataFrame(name_dict)
    # print(df)
    dir_path = 'Feature_Result'
    csv_filename = test + '.csv'
    csv_path = os.path.join(dir_path, csv_filename)
    df.to_csv(csv_path) # relative position

    data = pd.read_csv(csv_path)
    # select all rows ignore last column 'riders'
    features = data.iloc[:, :-1]
    # select all rows ignore all columns except lst one 'riders'
    labels = data.iloc[:, -1:]
# Create an untrained model and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(features, labels)
    feat_importance = model.feature_importances_
    importance = np.delete(feat_importance, [0])

    bike = ['BKF-BL', 'BKF-NGW', 'BKF-OFFSET', 'BKF-PBL', 'BKF-SHW']
    np.array(bike)
    plt.figure(num)
    plt.bar(bike, importance)
    plt.xlabel("Bike Infrastructure")
    plt.title(test + " Feature Importances")
    image_name = test + '.png'
    image_path = os.path.join(dir_path, image_name)
    plt.savefig(image_path)
    print(importance)


def main():
    name_dict1 = {
    # 'Year': [2015, 2016, 2018, 2019, 2020, 2021],
    'BKF-BL': [3, 23, 23, 23, 23, 23],
    'BKF-NGW': [28, 2, 13, 35, 35, 15],
    'BKF-OFFSET': [2, 2, 2, 2, 2, 2],
    'BKF-PBL': [2, 2, 2, 2, 8, 8],
    'BKF-SHW': [7, 7, 7, 7, 7, 7],
    'Riders': [342540, 326943, 316987, 357282, 311292, 264103]
    }
    name_dict2 = {
        # 'Year': [2014, 2015, 2020, 2021],
        'BKF-BL': [224, 237, 237, 237],
        'BKF-NGW': [34, 54, 54, 57],
        'BKF-OFFSET': [1, 3, 3, 3],
        'BKF-PBL': [214, 214, 216, 216],
        'BKF-SHW': [0, 0, 4, 4],
        'Riders': [6769, 6616, 13440, 11357]
    }
    name_dict3 = {
        # 'Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'BKF-BL': [142, 142, 142, 142, 142, 142, 142, 142],
        'BKF-NGW': [12, 69, 90, 93, 93, 99, 110, 118],
        'BKF-OFFSET': [0, 0, 0, 0, 0, 0, 0, 0],
        'BKF-PBL': [39, 40, 43, 47, 47, 54, 56, 56],
        'BKF-SHW': [7, 7, 7, 7, 7, 7, 7, 7],
        'Riders': [375061, 345642, 301097, 306970, 307648, 307342, 225966, 165491]
    }
    name_dict4 = {
        # 'Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'BKF-BL': [118, 119, 120, 120, 120, 120, 120, 120],
        'BKF-NGW': [38, 38, 41, 41, 41, 44, 44, 46],
        'BKF-OFFSET': [0, 0, 0, 0, 0, 0, 0, 0],
        'BKF-PBL': [7, 36, 58, 73, 73, 89, 89, 89],
        'BKF-SHW': [93, 93, 93, 93, 93, 93, 93, 93],
        'Riders': [375061, 345642, 301097, 306970, 307648, 307342, 225966, 165491]
    }
    name_dict6 = {
        # 'Year': [2014, 2015, 2016, 2017, 2018, 2019],
        'BKF-BL': [172, 183, 183, 183, 183, 183],
        'BKF-NGW': [20, 53, 53, 68, 87, 87],
        'BKF-OFFSET': [2, 2, 2, 2, 2, 2],
        'BKF-PBL': [36, 45, 47, 47, 47, 49],
        'BKF-SHW': [101, 101, 101, 101, 101, 101],
        'Riders': [205563, 62055, 42056, 39712, 40308, 39973]
    }
    name_dict7 = {
        # 'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'BKF-BL': [110, 110, 115, 115, 116, 116, 116],
        'BKF-NGW': [0, 0, 0, 0, 0, 0, 0],
        'BKF-OFFSET': [3, 5, 6, 6, 6, 6, 6],
        'BKF-PBL': [48, 51, 89, 108, 129, 137, 139],
        'BKF-SHW': [172, 172, 172, 172, 172, 172, 173],
        'Riders': [2601263, 2607327, 2555394, 2856935, 3382587, 1579167, 1346269]
    }
    print("test")

    make_feature(name_dict1, 'Distrcit1', 1)
    make_feature(name_dict2, 'District2', 2)
    make_feature(name_dict3, 'District3', 3)
    make_feature(name_dict4, 'District4', 4)
    make_feature(name_dict6, 'District6', 5)
    make_feature(name_dict7, 'District7', 6)
    


if __name__ == "__main__":
    main()