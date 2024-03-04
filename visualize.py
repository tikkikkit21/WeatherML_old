import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from datetime import datetime
from train import time_to_int

# check for provided version in cline args
VERSION = 1
if len(sys.argv) == 1:
    pass # TODO: get latest from json
else:
    arg = sys.argv[1]
    if arg == '-h':
        print("Usage: visualize.py [version]")
        exit()
    VERSION = arg  
DATA_CSV = f'data/weather_data_v{VERSION}.csv'

data = None

def init_data():
    global data
    
    labels = ['Date', 'Temp', 'FeelsLike', 'Humidity', 'UV', 'Wind', 'Label', 'Rain?']
    data = pd.read_csv(DATA_CSV, names=labels, skiprows=1)
    data['Date'] = data['Date'].apply(lambda d: time_to_int(d))
    data['Humidity'] = data['Humidity'].apply(lambda h: float(h.strip('%'))/100)

def label_hist():
    x = data.iloc[:,:-1]
    y = data['Outer Clothing']

    y.value_counts().sort_index().plot.bar(x='Label', y='# Occurences')
    plt.show()

def time_hist():
    times = data['Date'].apply(lambda d: time_to_int(d))

    times.plot.hist(bins=24)
    plt.title('Time Frequency')
    plt.ylabel('Count #')
    plt.xlabel('24hr Time (HHMM)')
    plt.show()

def scatter(feature='Temp'):
    colors = ['blue', 'green', 'yellow', 'red']
    clothes_cm = ListedColormap(colors)
    
    plt.scatter(
        x=data.index,
        y=data[feature],
        c=data['Label'].astype('category').cat.codes,
        cmap=clothes_cm
    )

    legend_labels = ['coat', 'jacket-long', 'jacket-short', 'none']
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i], markersize=10) for i in range(4)]
    plt.legend(legend_handles, legend_labels, title='Categories')

    plt.title(feature)
    plt.show()

if __name__ == '__main__':
    init_data()
    label_hist()
    time_hist()
    scatter('Temp')
    scatter('FeelsLike')
    scatter('Humidity')
    scatter('UV')
    scatter('Wind')
