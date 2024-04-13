import os
from datetime import datetime
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
from util import percent, time_to_int

MODEL_PATH = 'results.best/best.model'
SCALER_PATH = 'results.best/best.scaler'

if not (os.path.isfile(MODEL_PATH) or os.path.isfile(SCALER_PATH)):
    print('Missing best model and/or scaler, please run train.py first!')
    exit()

model: LogisticRegression = joblib.load(MODEL_PATH)
scaler: StandardScaler = joblib.load(SCALER_PATH)

def predict(*args):
    labels = ["time","temp","feels_like","humidity","uv","wind"]

    now = datetime.now().strftime("%H:%M")
    args = [time_to_int(now)] + list(args)

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
