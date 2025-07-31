try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result is: ", result)
    print("Result again is: ", result)
except ZeroDivisionError:
    print("Error! You cannot divide by 0")
except ValueError:
    print("Please enter valid number")
except NameError as ex:
    print("Name error is:", ex)
except Exception as ex:
    print('Oops! Unexpected error occured')
finally:
    print("program is completed")