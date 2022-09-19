import turtle
lenght = int(input("Zadejte delku: "))
t = turtle.Turtle()  
def ctverec():
    for i in range(4):
        t.forward(lenght)
        t.left(90)

ctverec()

t.penup()
t. goto(-200,0)
t.pendown()

ctverec()