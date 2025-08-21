my_dict = {
    'fruits':2,
    'apple':3,
    'banana':4,
    'watermelon':2

}
k = 3
res= {}
for key, value in my_dict.items():
    if my_dict[key] == k:
        res[key] = value
print(res)