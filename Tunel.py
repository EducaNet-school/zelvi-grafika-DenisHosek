import turtle

t = turtle.Turtle()
delka = 0
umisteni = 0
umisteni2 = 0
while True:
    t.penup()
    t.goto(umisteni,umisteni2)
    t.pendown()
    delka += 8
    umisteni -= 4
    umisteni2 -= 4
    for i in range(4):
      t.forward(delka)
      t.left(90)