import math
def circumference(radius):
    return 2 * math.pi * radius
radius = float(input("Enter the radius: "))
circumference = circumference(radius)
print("Circumference of circle is: ", round(circumference))

    