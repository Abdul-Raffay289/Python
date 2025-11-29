# Program to find average speed of three cyclists
# and check who is riding slower than the average
# Taking input speeds from the user
s1 = float(input("Enter speed of cyclist 1 (km/h): "))
s2 = float(input("Enter speed of cyclist 2 (km/h): "))
s3 = float(input("Enter speed of cyclist 3 (km/h): "))
# Calculating average speed
average_speed = (s1 + s2 + s3) / 3
print("\nAverage Speed =", average_speed, "km/h")
# Checking each cyclist
print("\nCyclists riding slower than average:")
if s1 < average_speed:
    print("Cyclist 1 is slower")
if s2 < average_speed:
    print("Cyclist 2 is slower")
if s3 < average_speed:
    print("Cyclist 3 is slower")
# If none are slower
if s1 >= average_speed and s2 >= average_speed and s3 >= average_speed:
    print("No cyclist is slower than average.")