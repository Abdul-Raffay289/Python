class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modernX1 = vehicle(240, 18)
print("Modern max speed", modernX1.max_speed)
print("Modern Mileage", modernX1.mileage)