number = int(input("Enter a number: "))

limit = int(input("How many powers do you want to see? ")) 

print("\nHere are the powers:")
for i in range(1, limit + 1):
    answer = number ** i
    print(f"{number} to the power of {i} is {answer}")
