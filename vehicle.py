class BMW:
    def fuel_type(self):
        print("BMW uses Diesel and Petrol")
    def max_speed(self):
        print("BMW max speed is 250 km/hr")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol")
    def max_speed(self):
        print("Ferrari max speed is 300 km/hr")

obj_bmw = BMW()
obj_ferrari = Ferrari()

for car in (obj_bmw, obj_ferrari):
    car.fuel_type()
    car.max_speed()
    print()