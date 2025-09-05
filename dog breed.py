class Dog:
    species = "Animal"
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

Tom = Dog("English Mastiff", "Brown")
Chase = Dog("German Shepherd", "Black")
print("Tom is a {}".format(Tom.breed))
print("Chase is a {}".format(Chase.breed))

print("Tom is {}".format(Tom.color))
print("Chase is {}".format(Chase.color))
