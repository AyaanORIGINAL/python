buying_price = int(input("Enter buying price:"))

selling_price = int(input("Enter selling price:"))

if buying_price > selling_price:
    loss = buying_price - selling_price
    print(f"loss: {loss}")
else:
    profit = selling_price - buying_price
    print(f"profit: {profit}")
