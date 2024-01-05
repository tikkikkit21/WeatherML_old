import matplotlib.pyplot as plot
import pandas as pd

data = pd.read_csv("weather_data_v1.csv")

def label_hist():
    x = data.iloc[:,:-1]
    y = data['Outer Clothing']

    y.value_counts().sort_index().plot.bar(x="Label", y="# Occurences")
    plot.show()
