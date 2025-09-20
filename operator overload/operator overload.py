class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return f"{other.a} is greater than {self.a}"
        else:
            return f"{self.a} is greater than {other.a}"

    def __eq__(self, other):
        if self.a == other.a:
            return f"{self.a} is equal to {other.a}"
        else:
            return f"{self.a} is not equal to {other.a}"
        
obj1 = A(6)
obj2 = A(7)
print("Passed values are", obj1.a, "and", obj2.a)
print(obj1 < obj2)
print(obj1 == obj2)