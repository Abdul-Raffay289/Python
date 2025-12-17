def factorial(x):
    '''This is recursive function to find factorial of an integer'''
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("Factorial of 1 is :  ", factorial(1))
print("Factorial of 2 is :  ", factorial(4))
print("Factorial of 5 is :  ", factorial(5))
print("Factorial of 10 is :  ", factorial(10))