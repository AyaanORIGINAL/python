temperature = input("Enter the temperature in Celsius: ")

temperature = float(temperature)

if temperature > 25:
    print("It's warm. You should wear light clothes like a T-shirt.")
elif temperature >= 15:
    print("It's a bit cool. A hoodie or light jacket will be good.")
else:
    print("It's cold. Wear heavy clothes like a sweater or coat.")
