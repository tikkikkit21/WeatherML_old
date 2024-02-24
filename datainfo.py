import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from train import time_to_int

data = None

def init_data():
    global data
    
    labels = ["Date", "Temp", "FeelsLike", "Humidity", "UV", "Wind", "Label", "Rain?"]
    data = pd.read_csv("weather_data_v1.csv", names=labels, skiprows=1)
    data["Date"] = data["Date"].apply(lambda d: time_to_int(d))
    data["Humidity"] = data["Humidity"].apply(lambda h: float(h.strip('%'))/100)

def label_hist():
    x = data.iloc[:,:-1]
    y = data['Outer Clothing']

    y.value_counts().sort_index().plot.bar(x="Label", y="# Occurences")
    plt.show()

def time_hist():
    times = data["Date"].apply(lambda d: time_to_int(d))

    times.plot.hist(bins=24)
    plt.title("Time Frequency")
    plt.ylabel("Count #")
    plt.xlabel("24hr Time (HHMM)")
    plt.show()

def scatter(feature="Temp"):
    plt.scatter(
        x=data.index,
        y=data[feature],
        c=data['Label'].astype('category').cat.codes,
        cmap='viridis'
    )
    plt.show()

if __name__ == "__main__":
    init_data()
    # label_hist()
    # time_hist()
    scatter("Temp")
    # scatter("FeelsLike")
    # scatter("Humidity")
    # scatter("UV")
    # scatter("Wind")
