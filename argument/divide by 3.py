def cube(number):
    return number ** 3

def divide_by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        print("Number is not divisible by 3")
 
num = int(input("Enter a number: "))
print (divide_by_three(num))