from abc import ABC, abstractmethod

class ABClass(ABC):
    def print(self,x):
        print("passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are in abstract task")

class test_class(ABClass):
    def task(self):
        print("Hello world task")

t1 = test_class()
t1.task()
t1.print(5)