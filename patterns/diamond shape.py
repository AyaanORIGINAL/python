rows = 5
space = rows -1

for i in range(1, rows+1):
    for j in range(1, space+1):
        print(end=" ")
    space -= 1

    for j in range (2*i -1):
        print(end='*')
    print()

space = 1
for i in range(1, rows):
    for j in range(1, space+1):
        print(" ", end="")
    space += 1
    for j in range (1, 2 *(rows - i)):
        print("*", end="")
    print()
    