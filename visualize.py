import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from util import time_to_int

# check for provided version in cline args
with open('data/version_info.json', 'r') as file:
    config = json.load(file)

if len(sys.argv) == 1:
    VERSION=list(config.keys())[-1]
else:
    arg = sys.argv[1]
    if arg == '-h':
        print('Usage: visualize.py [version number]')
        exit()
    elif not arg.isdigit():
        print('Version needs to be a number!')

    VERSION = f'v{arg}'

try:
    config = config[VERSION]
except KeyError:
    print(f'Dataset {VERSION} does not exist')
    exit()

DATA_CSV = f'data/weather_data_{VERSION}.csv'
data = None

def init_data():
    global data
    
    data = pd.read_csv(DATA_CSV, names=config['labels'], skiprows=1)
    data.drop(config['drop'], axis='columns', inplace=True)
    data['time'] = data['time'].apply(lambda d: time_to_int(d))
    data['humidity'] = data['humidity'].apply(lambda h: float(h.strip('%'))/100)

def label_hist():
    x = data.iloc[:,:-1]
    y = data[config['output']]

    y.value_counts().sort_index().plot.bar(x='Label', y='# Occurences')
    plt.show()

def time_hist():
    data['time'].plot.hist(bins=24)
    plt.title('Time Frequency')
    plt.ylabel('Count #')
    plt.xlabel('24hr Time (HHMM)')
    plt.show()

def scatter(feature='temp'):
    colors = ['blue', 'green', 'yellow', 'red']
    clothes_cm = ListedColormap(colors)
    
    plt.scatter(
        x=data.index,
        y=data[feature],
        c=data[config['output']].astype('category').cat.codes,
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
    scatter('temp')
    scatter('feels_like')
    scatter('humidity')
    scatter('uv')
    scatter('wind')
