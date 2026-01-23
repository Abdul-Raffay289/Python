from abc import ABC, abstractmethod
class ABS(ABC):
    def print(self, x):
        print("Passed Value", x)
    @abstractmethod
    def task(self):
        print("We are inside ABS class task")
class test(ABS):
    def task(self):
        print("We are inside test class task")
objtest = test()
objtest.task()
objtest.print(100)