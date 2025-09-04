class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

mithu = Parrot("Mithu", 5)
blu = Parrot("Blu", 100)

print("Mithu is a {}".format(mithu.species))
print("Blu is a {}".format(blu.species))

print("{} is {} years old".format(mithu.name, mithu.age))
print("{} is {} years old".format(blu.name, blu.age))