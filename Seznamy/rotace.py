import random
sez=[1,2,3,4,5,6]
x = int(input('Okolik se ma seznam otocit'))
sez = sez[x:] + sez[:x]
print(sez)

random = round(random.uniform(0,4))
sez = sez[random:] + sez[:random]
print(sez)






