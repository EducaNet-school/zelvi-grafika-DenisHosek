import turtle

t = turtle.Turtle()  
def ctverec():
    for i in range(4):
        t.forward(100)
        t.left(90)

ctverec()

t.penup()
t. goto(-200,0)
t.pendown()

ctverec()