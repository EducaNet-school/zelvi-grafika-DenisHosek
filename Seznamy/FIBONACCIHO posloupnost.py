opak = int(input('Zadejte cislo: '))
zlato = 1.618
seznam = []
od = 5 **(1/2)
for i in range(opak):
    f = round((zlato**(i) -(1-zlato)**(i)) / od)
    seznam.append(f)

print(seznam)
