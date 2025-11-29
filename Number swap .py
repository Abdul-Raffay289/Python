# Program to swap three numbers
# Taking input from the user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))
print("\nBefore swapping:")
print("a =", a, " b =", b, " c =", c)
# Swapping values (a → b, b → c, c → a)
temp = a
a = b
b = c
c = temp
print("\nAfter swapping:")
print("a =", a, " b =", b, " c =", c)