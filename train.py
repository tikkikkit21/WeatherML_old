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
with open('data/experiment_config.json', 'r') as file:
    config = json.load(file)

if len(sys.argv) == 1:
    VERSION=list(config.keys())[-1]
else:
    arg = sys.argv[1]
    if arg == '-h':
        print('Usage: train.py [version number]\nEx: train.py 2')
        exit()
    elif not arg.isdigit():
        print('Version needs to be a number!')
        exit()
    VERSION = f'exp{arg}'

try:
    config = config[VERSION]
except KeyError:
    print(f'Experiment \'{VERSION}\' does not exist')
    exit()

RESULTS_DIR = 'results'
BEST_DIR = 'results.best'
DATA_CSV = f'data/{config["dataset"]}'

if __name__ == '__main__':
    model = LogisticRegression(solver='liblinear', multi_class='ovr')
    scaler = StandardScaler()

    # prepare dataset
    data = pd.read_csv(DATA_CSV, names=config['labels'], skiprows=1)
    data['time'] = data['time'].apply(lambda d: time_to_int(d))
    data['humidity'] = data['humidity'].apply(lambda h: float(h.strip('%'))/100)

    # split into test/train
    train = data.drop(columns=config['ignore'])
    x = train[train.drop(columns=config['output']).columns.tolist()]
    y = train[config['output']]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)    

    # standardize
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    # train
    model.fit(x_train, y_train)

    # score model
    print('Train accuracy:', percent(model.score(x_train, y_train)))
    print('Test accuracy:', percent(model.score(x_test, y_test)))

    # store 
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    timestamp = f'{datetime.now().date()}_{datetime.now().time().strftime("%M%H%S")}'
    joblib.dump(model, f'{RESULTS_DIR}/{timestamp}.model')
    joblib.dump(scaler, f'{RESULTS_DIR}/{timestamp}.scaler')

    # prompt to save in best
    save = input('Would you like to save this run as your best? (y/N) ').lower()
    save = save in ['y', 'yes']
    if save:
        if not os.path.exists(BEST_DIR):
            os.makedirs(BEST_DIR)
        joblib.dump(model, f'{BEST_DIR}/best.model')
        joblib.dump(scaler, f'{BEST_DIR}/best.scaler')
        print(f'Results saved in \'{BEST_DIR}\'')
    else:
        print('Note: Results are still saved in your \'results\' folder')
