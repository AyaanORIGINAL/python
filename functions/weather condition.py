def weather_condition():
    weather = input("Enter the weather condition:")
    if weather.lower() == "sunny":
        print("Wear light clothes")
    elif weather.lower() == "rainy":
        print("Wear a raincoat and carry umbrella")
    elif weather.lower() == "cloudy":
        print("Wear light clothes")
    elif weather.lower() == "snowy":
        print("Wear warm clothes")
    else:
        print("Invalid")

weather_condition()
