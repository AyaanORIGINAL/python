class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h, Mileage: {self.mileage} km/l")

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h, Mileage: {self.mileage} km/l, Capacity: {self.capacity} passengers")

schoolbus = Bus("School Volvo", 180, 12, 50)
schoolbus.display()