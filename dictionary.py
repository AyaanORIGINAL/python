my_dict = {
    "Codingal": 3,
    "is": 2,
    "best": 2,
    "for": 2,
    "coding": 1
}

freq = int(input("Enter a number to find its frequency: "))
res= {}
for key, value in my_dict.items():
    if my_dict[key] == freq:
        res[key] = value
print(res)
