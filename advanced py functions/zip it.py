s1 = {3,2,1}
s2 = {'b','a','c'}

s3 = zip(s1,s2)
print(list(s3))

list1 = [10,20,30,40,50]
list2 = [100,200,300,400,500]

for x,y in zip(list1,list2):
    print(x,y)

even = [x for x in range (1,11) if x % 2 == 0]
print(even)

stocks = ['bata', 'apex', 'bay']
prices = [2000,2100,1500]

newdict ={stocks: prices for stocks, prices in zip(stocks, prices)}
print(newdict)