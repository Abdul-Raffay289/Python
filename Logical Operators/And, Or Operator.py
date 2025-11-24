a = 10
b = 12
c = 0
if a and b and c:
    print("Yes! all the values are true")
else:
    print("No! all the values are false")
# or operator
a = 10
b = -10
c = 0
if a > b or b > c or a > c:
    print("True")
else:
    print("False")
a = -10
b = 10
c = -1
if a > b or b < c or a > c:
    print("True")
else:
    print("False")
#Not equal 
a = 10
b = 12
c = 12
print(a != b)
print(b != c)
a = "python"
b = "coding"
if a != b:
    print("Both are different")