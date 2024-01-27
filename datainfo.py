import matplotlib.pyplot as plot
import pandas as pd
from datetime import datetime
from model import time_to_int

labels = ["Date", "Temp", "FeelsLike", "Humidity", "UV", "Wind", "Label", "Rain?"]
data = pd.read_csv("weather_data_v1.csv", names=labels, skiprows=1)
data["Date"] = data["Date"].apply(lambda d: time_to_int(d))
data["Humidity"] = data["Humidity"].apply(lambda h: float(h.strip('%'))/100)

def label_hist():
    x = data.iloc[:,:-1]
    y = data['Outer Clothing']

    y.value_counts().sort_index().plot.bar(x="Label", y="# Occurences")
    plot.show()

def time_hist():
    times = data["Date"].apply(lambda d: time_to_int(d))

    times.plot.hist(bins=24)
    plot.title("Time Frequency")
    plot.ylabel("Count #")
    plot.xlabel("24hr Time (HHMM)")
    plot.show()

def scatter(label="Temp"):
    data.plot.scatter(x=label, y="Label")
    plot.show()

# label_hist()
# time_hist()
scatter("Temp")
scatter("FeelsLike")
scatter("Humidity")
scatter("UV")
scatter("Wind")
