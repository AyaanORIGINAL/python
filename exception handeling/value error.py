try:
    num = int(input("Enter a number: " ))
    print(num)
except ValueError as ve:
    print("Invalid input: ", ve )