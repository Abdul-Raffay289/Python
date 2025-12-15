def add(num1, num2):
    return(num1 + num2)
def sub(num1, num2):
    return(num1 - num2)
def multiply(num1, num2):
    return(num1 * num2)
def divide(num1, num2):
    return(num1 / num2)
print("Please selct the operation")
print("a)add)")
print("b)sub)")
print("c)multiply)")
print("d)divide)")
choice = input("Enter your choice: a, b , c or d: ")
num_1 = int(input("Enter you first num: "))
num_2 = int(input("Enter you second num: "))
if choice == 'a':
    print(add(num_1, num_2))
elif choice == 'b':
    print(sub(num_1, num_2))
elif choice == 'c':
    print(multiply(num_1, num_2))
elif choice == 'd':
    print(divide(num_1, num_2))
else:
    print("This is an invalid input")