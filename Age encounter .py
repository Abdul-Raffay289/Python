try:
    age = int(input("Enter your age: "))

    if age <= 0:
        raise ValueError("Age must be a positive number")

    print("Age is valid.")

    if age % 2 == 0:
        print("The entered age is Even.")
    else:
        print("The entered age is Odd.")

except ValueError as e:
    print("Invalid input!", e)
