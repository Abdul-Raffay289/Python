class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
Woo = parrot("Woo", 2)
Blu = parrot("Blu", 2)
print("Blu is a", Blu.species)
print("Woo is a", Woo.species)
print("{} is {} years old", format(Blu.name, Blu.age))
print("{} is {} years old", format(Woo.name, Woo.age))