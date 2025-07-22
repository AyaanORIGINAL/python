def add (a,b):
    return (a + b)

def subtract (a,b):
    return (a - b)

def multiply (a,b):
    return (a * b)

def divide (a,b):
    if b == 0:
        print("Number cannot be divided by 0")
    else:
        return (a / b)
    
print("a.Add")
print("b. Subtract")
print ("c. Multiply")
print ("d. Divide")

choice = input("Enter your choice (a, b, c, d): ")
num1 = float (input("Enter first number: "))
num2 = float (input("Enter second number: "))

if choice == "a":
   print(num1, "+", num2, "=", add(num1, num2) )
elif choice == "b":
   print(num1, "-", num2, "=", subtract(num1, num2) )
elif choice == "c":
    print(num1, "*", num2, "=", multiply(num1, num2) )
elif choice == "d":
    print(num1, "/", num2, "=", divide(num1, num2) )
else:
    print("Invalid! please choose a, b, c or d")
    