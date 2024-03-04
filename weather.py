from datetime import datetime

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

from util import percent

model: LogisticRegression = joblib.load('results/2024-02-24_561133.model')
scaler: StandardScaler = joblib.load('results/2024-02-24_561133.scaler')

def predict(*args):
    labels = ['Date', 'Temp', 'FeelsLike', 'Humidity', 'UV', 'Wind', 'Label', 'Rain?']

    now = datetime.now().time().strftime('%H%M')
    args = [int(now)] + list(args)

    df = pd.DataFrame([args], columns=labels[:6])
    sample = scaler.transform(df)
    
    print('Prediction:', model.predict(sample))
    print('Confidence:', percent(max(model.predict_proba(sample)[0])))


if __name__ == '__main__':
    print('Welcome to WeatherML!')

    temp = input('What is the actual temperature (°F)? ')
    feelsLike = input('What is the feels like temperature (°F)? ')
    humidity = input('What is the humidity (%)? ')
    humidity = int(humidity) / 100
    uv = input('What is the UV? ')
    wind = input('What is the wind speed (mph)? ')
    
    print()
    predict(temp, feelsLike, humidity, uv, wind)
