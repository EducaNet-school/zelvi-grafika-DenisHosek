import turtle

pocet = int(input("Pocet lupenu: "))
if  6 == pocet:
    stupne = 180 // pocet
elif (pocet % 4) == 0 :
    stupne = (5/4) * pocet
elif (pocet % 7) ==0:
    stupne = 280 // pocet
elif (pocet % 5) ==0:
    stupne = 150 // pocet
else:
    stupne = 360 // pocet



t=turtle.Turtle()

def elipsa():
    t.circle(100,90)
    t.left(90)
    t.circle(100,90)

for i in range(pocet):
   elipsa()  
   t.left(stupne)
