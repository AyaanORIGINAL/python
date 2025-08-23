import array as arr

num = arr.array("i", [1,2,3,4,5,6,5,4,2,6,7])
print(num)

print("Occurance of 6: ", num.count(6))

num.append(6)
print(num)

num.remove(5)
print(num)

num.extend([0,6,7])
print(num)

num.reverse()
print(num)

num.clear()
print(num)