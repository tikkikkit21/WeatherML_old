import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

RESULTS_DIR = 'results'
DATA_CSV = 'data/weather_data_v1.csv'

def percent(num):
    return format(num, '.2%')

def time_to_int(timeString):
    timeObj = datetime.strptime(timeString, '%H:%M').time()
    timeInt = timeObj.hour * 60 + timeObj.minute
    return timeInt

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
