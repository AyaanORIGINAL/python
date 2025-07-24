def tip_waiter(bill_amount, tip_percentage):
    total = bill_amount + bill_amount * (tip_percentage / 100)
    total = round (total, 2)
    print("Total bill amount is: ", total)

tip_waiter (200,10)