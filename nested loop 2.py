size = 5

print("Multiplication Table:")

for i in range(1, size + 1):
    for j in range(1, size + 1):
        product = i * j
        print(f"{product:4}", end="") 
    print() 