import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# prepare dataset
labels = ["Date", "Temp", "FeelsLike", "Humidity", "UV", "Wind", "Label", "Rain?"]
data = pd.read_csv("weather_data_v1.csv", names=labels, skiprows=1)

data["Date"] = data["Date"].apply(lambda d: datetime.strptime(d, '%m/%d/%Y %H:%M'))
data["Date"] = data["Date"].apply(lambda d: int(d.time().strftime('%H%M')))
data["Humidity"] = data["Humidity"].apply(lambda h: float(h.strip('%'))/100)
data = data.drop("Rain?", axis=1)

# split into test/train
x = data[data.columns.tolist()[:-1]]
y = data["Label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)

# standardize
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# train
model = LogisticRegression(solver="liblinear", multi_class="ovr")
model.fit(x_train, y_train)

# score model
print("Train accuracy:", model.score(x_train, y_train))
print("Test accuracy:", model.score(x_test, y_test))
print()

# make predictions
test = x_test[0].reshape(1,-1)
print("Prediction:", model.predict(test))
print("Confidence:", max(model.predict_proba(test)[0]))
