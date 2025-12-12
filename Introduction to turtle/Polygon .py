import turtle
turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()
sides = int(input("Enter number of sides of Polygon: "))
pixels = int(input("Enter the lenght of Polygon: "))
angle = 360/sides
for i in range (sides):
    polygon.forward(pixels)
    polygon.right(angle)
turtle.done()