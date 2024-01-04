import model

if __name__ == "__main__":
    print("Welcome to WeatherML!")
    print("Training model...")
    model.train()
    model.predict(80, 80, 0.44, 9, 4)
