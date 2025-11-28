num_1 = int(input("Enter the numerator "))
num_2 = int(input("Enter the denominator "))
num_3 = num_1/num_2
num_4 = num_1%num_2
print("The answer is", num_3)
print("The reminder is", num_4)
if num_1%num_2==0:
    print("It is an Divisible number.")
else:
    print("It is not Divisible number.")