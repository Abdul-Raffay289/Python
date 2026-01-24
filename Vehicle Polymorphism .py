class BMW:
    def popular(self):
        print("BMW is very popular car")
class Ferrari:
    def fastest(self):
        print("Ferrari is the fastest car")
obj_BMW = BMW
obj_Ferrari = Ferrari
for car in(obj_BMW, obj_Ferrari):
    car.popular()
    car.fastest()