print ("Using while loop")
i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(j, end=" ")
        j += 1
    i += 1
    print()

print ("Using for loop")
for i in range(5):
    for j in range (1, 11):
        print(j, end=" ")
    print()