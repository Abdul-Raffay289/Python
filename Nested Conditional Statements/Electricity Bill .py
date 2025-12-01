units = int(input("Enter the units to calculate bill: "))
if units <= 50:
    amount = units * 3.60
    surcharge = 25
elif units <= 100:
    amount = units * 3.25
    surcharge = 35
elif units <= 200:
    amount = units * 5.26
    surcharge = 45
else:
    amount = units * 8.25
    surcharge = 75
total = amount + surcharge
print("Your total bill is", total)