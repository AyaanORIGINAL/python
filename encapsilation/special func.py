class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    def __len__(self):
        distance = (self.x**2 + self.y**2)**0.5
        return int(distance)

p1 = Point(5,8)
p2 = Point(5,2)
print("p1:", p1)
print("p2:", p2)
p3 = p1 + p2
print("p1 + p2:", p3)

print(f"The distance of {p1} from origin 0,0 is approximately {len(p1)}")
print(f"The distance of {p2} from origin 0,0 is approximately {len(p2)}")