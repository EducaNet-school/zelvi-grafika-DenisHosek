import turtle

t = turtle.Turtle()

lenght = int(input("Zadejte delku: "))

for i in range(3):
     t.left(125)
     for i in range(4):
        t.forward(lenght)
        t.left(90)

