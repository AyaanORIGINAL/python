amount = int(input("Enter the amount: "))

note500 = amount // 500
amount = amount % 500
note100 = amount // 100
amount = amount % 100
note50 = amount // 50
amount = amount % 50
note20 = amount // 20
amount = amount % 20

print("Note of 500:", note500)
print("Note of 100:", note100)
print("Note of 50:", note50)
print("Note of 20:", note20)
print("Remaining amount: ", amount)