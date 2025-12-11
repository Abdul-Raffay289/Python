Num = int(input("Enter a decimal to convert it into Binary Numbers: "))
n = Num
Binary = ""
while n > 0:
    remainder = Num % 2 
    for j in range(1):
        Binary = str(remainder) + Binary
    n = n//2
    print("Binary of", Num, "is:", Binary)