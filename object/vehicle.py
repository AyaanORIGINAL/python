class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    

v1 = Vehicle(200,12)
print("Max speed is,", v1.max_speed)
print("Mileage speed is,", v1.mileage)