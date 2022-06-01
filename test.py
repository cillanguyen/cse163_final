import pandas as pd
import matplotlib.pyplot as plt
import pickle


# with open('Data/refined_data/existing_facilities_data.pickle', 'rb') as f:
#     df = pickle.load(f)
#     # print(df.columns)
#     df = df[['CATEGORY', 'INSTALL_DATE', 'PRIMARYDISTRICTCD','SHAPE_Length']]
#     mask1 = df['PRIMARYDISTRICTCD']=='DISTRICT2'
#     mask2 = df['INSTALL_DATE'] == '2015'
#     data = df[mask1 & mask2]
#     # print(data)
#     print(data)
with open('Data/refined_data/total_bike_counters.pickle', 'rb') as f:
    df = pickle.load(f)
    data = df[df['council_district']==7]
    print(data)
    