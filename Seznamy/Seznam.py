seznam = []
opak = 10

for i in range(opak):
    cislo = int(input('Zadejte cislo'))
  

    if (cislo % 2) == 0:
        cislo -= 1
        seznam.append(cislo)
    else:
        seznam.append(cislo)

print(seznam)
cislo = sum(seznam)
prum = cislo / opak

print(round(prum, 2))