import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def percent(num):
    return format(num, ".2%")

def time_to_int(dateString):
    dateObj = datetime.strptime(dateString, '%m/%d/%Y %H:%M')
    dateInt = int(dateObj.time().strftime('%H%M'))
    return dateInt

model = LogisticRegression(solver="liblinear", multi_class="ovr")
labels = ["Date", "Temp", "FeelsLike", "Humidity", "UV", "Wind", "Label", "Rain?"]
scaler = StandardScaler()

# prepare dataset
data = pd.read_csv("weather_data_v1.csv", names=labels, skiprows=1)
data["Date"] = data["Date"].apply(lambda d: time_to_int(d))
data["Humidity"] = data["Humidity"].apply(lambda h: float(h.strip('%'))/100)
data = data.drop("Rain?", axis=1)

# split into test/train
x = data[data.columns.tolist()[:-1]]
y = data["Label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)    

# standardize
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# train
model.fit(x_train, y_train)

# score model
print("Train accuracy:", percent(model.score(x_train, y_train)))
print("Test accuracy:", percent(model.score(x_test, y_test)))

# def predict(*args):
#     now = datetime.now().time().strftime('%H%M')
#     args = [int(now)] + list(args)

#     df = pd.DataFrame([args], columns=labels[:6])
#     sample = scaler.transform(df)
    
#     print("Prediction:", model.predict(sample))
#     print("Confidence:", percent(max(model.predict_proba(sample)[0])))
