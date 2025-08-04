bill_amount = float(input("Whats the amount of the bill? "))
paid_amount = float(input("How much did you pay? "))
due_amount = paid_amount - bill_amount
print("The cashier will return", due_amount, "to you")
