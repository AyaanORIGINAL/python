import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius)


if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    circle1 = Circle(r)

    print(f"Radius: {circle1.radius}")
    print(f"Area: {circle1.area()}")
    print(f"Perimeter: {circle1.perimeter()}")

