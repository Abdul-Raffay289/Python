height = (float(input("Enter your height here: ")))
weight = (float(input("Enter your weight here: ")))
BMI = weight / (height)**2
print("Your BMI is", BMI)
if BMI <= 18.4:
    print("Under weight")
elif BMI <= 24.9 :
    print("Healthy weight")
elif BMI <= 29.9:
    print("Over weight")
elif BMI <= 34.9:
    print("severly over weight")
elif BMI <= 39.9:
    print("Obese")
else:
    print("severly obese")