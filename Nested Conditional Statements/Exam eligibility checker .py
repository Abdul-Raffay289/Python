medical_cause = input("Do you have a medical cause Y or N: ")
atten = int(input("Enter your attendence: "))
if medical_cause == 'Y':
    print("You can give exam")
else:
    if atten >= 75:
        print("Your attendence is above 75, so you can give exam")
    else:
        print("You are not allowed to give exam")