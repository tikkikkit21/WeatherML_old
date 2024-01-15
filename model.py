import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def percent(num):
    return format(num, ".2%")

class WeatherML:
    def __init__(self):
        self.model = LogisticRegression(solver="liblinear", multi_class="ovr")
        self.labels = ["Date", "Temp", "FeelsLike", "Humidity", "UV", "Wind", "Label", "Rain?"]
        self.scaler = StandardScaler()

    def train(self):
        # prepare dataset
        data = pd.read_csv("weather_data_v1.csv", names=self.labels, skiprows=1)

        data["Date"] = data["Date"].apply(lambda d: datetime.strptime(d, '%m/%d/%Y %H:%M'))
        data["Date"] = data["Date"].apply(lambda d: int(d.time().strftime('%H%M')))
        data["Humidity"] = data["Humidity"].apply(lambda h: float(h.strip('%'))/100)
        data = data.drop("Rain?", axis=1)

        # split into test/train
        x = data[data.columns.tolist()[:-1]]
        y = data["Label"]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)    

        # standardize
        self.scaler.fit(x_train)
        x_train = self.scaler.transform(x_train)
        x_test = self.scaler.transform(x_test)

        # train
        self.model.fit(x_train, y_train)

        # score model
        print("Train accuracy:", percent(self.model.score(x_train, y_train)))
        print("Test accuracy:", percent(self.model.score(x_test, y_test)))
        print()

    def predict(self, *args):
        now = datetime.now().time().strftime('%H%M')
        args = [int(now)] + list(args)

        df = pd.DataFrame([args], columns=self.labels[:6])
        sample = self.scaler.transform(df)
        
        print("Prediction:", self.model.predict(sample))
        print("Confidence:", percent(max(self.model.predict_proba(sample)[0])))
