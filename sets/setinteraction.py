set1 = {'green', 'red'}
set2 = {"green", "blue"}
print(set1.intersection(set2))
print(set1.union(set2))

difference = set1.difference(set2)
print(difference)

difference = set2.difference(set1)
print(difference)