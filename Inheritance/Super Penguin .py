class Bird:
    def __init__(self):
        print("Bird is ready!")
    def Who_Is_This(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super(). __init__()
        print("Bird is ready!")
    def Who_Is_This(self):
        print("Penguin")
    def run(self):
        print("Run fast")
Peggy = Penguin()
Peggy.Who_Is_This()
Peggy.swim()
Peggy.run()