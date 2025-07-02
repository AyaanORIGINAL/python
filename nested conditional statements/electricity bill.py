units = int( input("Enter the number of units consumed: "))

if units <=50 :
    amount = units * 2.60
    tax = 25
elif units <=100:
    amount = units * 3.25
    tax = 50
elif units <=150:
    amount = units * 4.50
    tax = 75
elif units <=200:
    amount = units * 5.75
    tax = 100
else:
    amount = units * 6.50
    tax = 125

total_amount = amount + tax
print("Total electricity bill is:", total_amount)