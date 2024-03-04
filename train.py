import os
import sys
import json
from datetime import datetime

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

from util import time_to_int, percent

# check for provided version in cline args
with open('data/version_info.json', 'r') as file:
    config = json.load(file)

if len(sys.argv) == 1:
    VERSION=list(config.keys())[-1]
else:
    arg = sys.argv[1]
    if arg == '-h':
        print('Usage: train.py [version number]')
        exit()
    elif not arg.isdigit():
        print('Version needs to be a number!')

    VERSION = f'v{arg}'

try:
    config = config[VERSION]
except KeyError:
    print(f'Dataset {VERSION} does not exist')
    exit()

RESULTS_DIR = 'results'
DATA_CSV = f'data/weather_data_{VERSION}.csv'

if __name__ == '__main__':
    model = LogisticRegression(solver='liblinear', multi_class='ovr')
    labels = ['Date', 'Temp', 'FeelsLike', 'Humidity', 'UV', 'Wind', 'Label', 'Rain?']
    scaler = StandardScaler()

    # prepare dataset
    data = pd.read_csv(DATA_CSV, names=labels, skiprows=1)
    data['Date'] = data['Date'].apply(lambda d: time_to_int(d))
    data['Humidity'] = data['Humidity'].apply(lambda h: float(h.strip('%'))/100)
    data = data.drop('Rain?', axis=1)

    # split into test/train
    x = data[data.columns.tolist()[:-1]]
    y = data['Label']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)    

    # standardize
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    # train
    model.fit(x_train, y_train)

    # store 
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    timestamp = f'{datetime.now().date()}_{datetime.now().time().strftime("%M%H%S")}'
    joblib.dump(model, f'results/{timestamp}.model')
    joblib.dump(scaler, f'results/{timestamp}.scaler')

    # score model
    print('Train accuracy:', percent(model.score(x_train, y_train)))
    print('Test accuracy:', percent(model.score(x_test, y_test)))
