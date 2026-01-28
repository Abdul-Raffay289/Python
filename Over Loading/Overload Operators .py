class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a < other.a):
            return"Ob1 is less than ob2"
        else:
            return"On2 is less than Ob1"
    def __eq__(self, other):
        if(self.a == other.a):
            return"Both are equal"
        else:
            return"Not Equal"
Ob1 = A(2)
Ob2 = A(3)
print("Passed Values", Ob1.a, Ob2.a)
print(Ob1<Ob2)
Ob3 = A(4)
Ob4 = A(4)
print("Passed Values", Ob3.a, Ob4.a)
print(Ob3==Ob4)