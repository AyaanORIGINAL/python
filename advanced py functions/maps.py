numbers1 = [1,2,3,4]
numbers2 = [5,6,7,8]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  

def square(n):
    return n * n
squared = map(square, numbers1)
print(list(squared))