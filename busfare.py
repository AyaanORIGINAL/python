class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1


bus = Bus(50)
print("Total Bus fare:", bus.fare(),"BDT")  
