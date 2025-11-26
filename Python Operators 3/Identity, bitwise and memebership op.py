#Identity Operator
num_1 = 5
num_2 = 2
if (type(num_1)is int):
    print("True")
else:
    print("False")
#membership operator
if num_1 not in [num_2]:
    print("True")
else:
    print("False")
#Bitwise operator
a = 10
b = 5
print(a<<b)
print(a>>b)
print(a&b)
print(a*b)
print(~b)
print(a|b)