class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
class Bus (vehicle):
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
BMW_M5 = Bus(200, 8)
print("Bus Max Speed and mileage: ", BMW_M5)