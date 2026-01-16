class Employee():
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Destructor called")
def create_object():
    print("making object")
    obj = Employee()
    print("Function end")
    return obj
print("Calling Obj Function")
obj = create_object()
print("Program end...")