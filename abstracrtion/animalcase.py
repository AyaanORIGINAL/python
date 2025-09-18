from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("Can move with 2 legs")

class Dog(Animal):
    def move(self):
        print("Can move with 4 legs")

class Snake(Animal):
    def move (self):
        print("Crawls with their body")

class Bird(Animal):
    def move(self):
        print("Can fly in the sky")

h = Human()
h.move()
d = Dog()
d.move()
s = Snake()
s.move()
b = Bird()
b.move()