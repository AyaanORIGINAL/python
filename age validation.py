try:
    age = int(input("Enter your age using numbers: "))
    print("Your age is", age)

except ValueError:
    print("Please enter valid number")
except NameError as ex:
    print("Name error is:", ex)