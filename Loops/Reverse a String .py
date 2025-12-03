string = input("Please enter your own string: ")
string_2 = ('')
for i in string:
    string_2 = i + string_2
print("\nThe original string is: ", string)
print("The reverse string is: ", string_2)