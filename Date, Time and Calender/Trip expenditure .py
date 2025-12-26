def hotel_cost(nights):
    return 140*nights
def ride_cost(city):
    if city == "Karachi":
        return 480
    elif city == "Lahore":
        return 380
    elif city == "Islamabad":
        return 400
def car_cost(days):
    if days >= 7:
        return 40*days - 50
    elif days >= 3:
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city, days, money):
    return car_cost(days) + hotel_cost(days) + ride_cost(city) + money
print("Car cost is", car_cost(7))
print("hotel cost is", hotel_cost(7))
print("ride cost is", ride_cost("Lahore"))
print(trip_cost("Lahore", 7, 7))