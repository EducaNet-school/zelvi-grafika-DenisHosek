import turtle

t = turtle.Turtle()
while True:
    for i in range(3):
        t.left(45)
        for i in range(4):
            t.forward(100)
            t.left(90)

