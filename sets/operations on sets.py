my_set = {1,2,3}
print(my_set)

my_set = {1,2,3,4,4,3,2,1,2,3,4,4}
print(my_set)

my_list = [1,2,3,4,4,3,2,1,2,3,4,4]
print(my_list)

my_set = set(my_list)
print(my_set)

for i in my_set:
    print(i)

my_set.add(5)
print(my_set)

my_set.remove(5)
print(my_set)

my_set.pop()
print(my_set)