n = int(input("Enter a number: "))

print('Reversed order: ')
for i in range (n, 0, -1):
    print(i)

print("Even numbers: ")
for i in range (2,n+1,2):
    print(i)
print("Odd numbers: ")
for i in range (1,n+1,2):
    print(i)