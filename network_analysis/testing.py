import pandas as pd

with open('Data\\refined_data\\existing_facilities_data_csv.csv') as f:
    df = pd.read_csv(f)


print(df.loc[0, 'INSTALL_DATE'] >= 2011)
