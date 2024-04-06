import sys
import json
import pandas as pd
import sklearn.decomposition
from util import time_to_int

with open('data/experiment_config.json', 'r') as file:
    config = json.load(file)

if len(sys.argv) == 1:
    VERSION=list(config.keys())[-1]
else:
    arg = sys.argv[1]
    if arg == '-h':
        print('Usage: analyze.py [version number]\nEx: analyze.py 2')
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

DATA_CSV = f'data/{config["dataset"]}'

data = pd.read_csv(DATA_CSV, names=config['labels'], skiprows=1)
data['time'] = data['time'].apply(lambda d: time_to_int(d))
data['humidity'] = data['humidity'].apply(lambda h: float(h.strip('%'))/100)

pca = sklearn.decomposition.PCA()
data_norm = data.drop(columns=config['ignore']).select_dtypes(include=['number'])
data_norm = (data_norm - data_norm.mean()) / data_norm.std()
tablePCA = pca.fit_transform(data_norm)
tablePCA = pd.DataFrame(tablePCA, index=data_norm.index)

print(data_norm.columns)
print(pca.explained_variance_ratio_)
