try:
    num_1, num_2 = eval(input("Enter 2 numbers using comma: "))
    result = num_1/num_2
    print("\nResult is:", result)
except ZeroDivisionError:
    print("\nDivision by zero is an error")
except SyntaxError:
    print("\nYou have forgot comma, so please write the number in comma")
except:
    print("\nWrong syntax")
else:
    print("\nNo exception")
finally:
    print("\nThe code will execute no matter what!") 