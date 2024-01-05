import matplotlib.pyplot as plot
import pandas as pd
from datetime import datetime

data = pd.read_csv("weather_data_v1.csv")

def label_hist():
    x = data.iloc[:,:-1]
    y = data['Outer Clothing']

    y.value_counts().sort_index().plot.bar(x="Label", y="# Occurences")
    plot.show()

def time_freq():
    times = data["Date/Time"].apply(lambda d: datetime.strptime(d, '%m/%d/%Y %H:%M'))
    times = times.apply(lambda d: int(d.time().strftime('%H%M')))
    times.plot.hist(bins=24)
    plot.show()

time_freq()
