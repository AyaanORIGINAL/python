L = [4,5,1,2,9,7,10,8]
print("Original list:", L)
sum = 0
for i in L:
    sum += i
avg = sum / len(L)

print("Sum:", sum)
print("Average:", avg)

L.sort()
print(L)

print("Smallest element is:", L[0])
print("Largest element is:", L[-1])