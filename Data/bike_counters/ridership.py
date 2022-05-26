"""
Creating combined ridership dataset.
"""
import pandas as pd
import matplotlib.pyplot as plt
# import pickle


def make_ts(filename):
    # Reading data file into DF:
    df = pd.read_csv(filename, index_col='Date', parse_dates=True)
    # Sorting date indices:
    df.sort_index()

    # Summing to annual data:
    annual = df.resample('A').sum()

    return annual


filepath = '\\2nd_Ave_Cycle_Track_North_of_Marion_St_Bicycle_Counter.csv'

data = make_ts(filepath)
data.plot(col='2nd Ave Cycletrack')

plt.savefig('plot.png')
