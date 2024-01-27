import matplotlib.pyplot as plot
import pandas as pd
from datetime import datetime
from model import time_to_int

data = pd.read_csv("weather_data_v1.csv")

def label_hist():
    x = data.iloc[:,:-1]
    y = data['Outer Clothing']

    y.value_counts().sort_index().plot.bar(x="Label", y="# Occurences")
    plot.show()

def time_freq():
    times = data["Date/Time"].apply(lambda d: time_to_int(d))

    times.plot.hist(bins=24)
    plot.title("Time Frequency")
    plot.ylabel("Count #")
    plot.xlabel("24hr Time (HHMM)")
    plot.show()

time_freq()
