import random
class fruit_quiz:
    def __init(self):
        self.fruits = {'Apple':'Red',
                       'Mango':'Yellow',
                       'Orange':'Orange',
                       'Watermelon':'Green'}
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of{}".format(fruit))
            if (user_answer.lower() == color):
                print("Correct color")
            else:
                print("Wrong answer")
            option = int(input("Enter 0 if you want to add another otherwise enter 1: "))
            if option:
                break
print("Welcome to fruit quiz")
fq = fruit_quiz()
fq.quiz()