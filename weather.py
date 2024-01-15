from model import WeatherML

if __name__ == "__main__":
    print("Welcome to WeatherML!")
    print("Training model...")
    model = WeatherML()
    model.train()

    temp = input("What is the actual temperature (°F)? ")
    feelsLike = input("What is the feels like temperature (°F)? ")
    humidity = input("What is the humidity (%)? ")
    humidity = int(humidity) / 100
    uv = input("What is the UV? ")
    wind = input("What is the wind speed (mph)? ")
    
    print()
    model.predict(temp, feelsLike, humidity, uv, wind)
