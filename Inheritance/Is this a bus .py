class vehicle:
    def __init__(self, name, maximum_speed, mileage):
        self.name = name
        self.maximum_speed = maximum_speed
        self.mileage = mileage
class Bus(vehicle):
    pass
School_bus = Bus("School Volvo", 135.3, 12)
print("Name:", School_bus.name, "Maximum speed:", School_bus.maximum_speed, "Mileage:", School_bus.mileage)