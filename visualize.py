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
    data['time'] = data['time'].apply(lambda d: time_to_int(d))
    data['humidity'] = data['humidity'].apply(lambda h: float(h.strip('%'))/100)

def label_hist(axis):
    output = data[config['output']].value_counts().sort_index()
    output.plot.bar(
        x='Label',
        y='# Occurences',
        ax=axis
    )

def time_hist(axis):
    data['time'].plot.hist(bins=24, ax=axis)

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

    fig, (ax1, ax2) = plt.subplots(
        nrows=1,
        ncols=2,
        figsize=(12,6)
    )

    time_hist(ax2)
    label_hist(ax1)
    plt.show()
    # scatter('temp')
    # scatter('feels_like')
    # scatter('humidity')
    # scatter('uv')
    # scatter('wind')
