def sou_lich(a):
    b = []
    c = 0
    if (a % 2) == 0:
        print("Cislo neni liche")
        print("Prosim zadejte nove cislo")
        a = int(input('Zadejte liche cislo: '))
        sou_lich(a)
    else:
        b.append(a)
        for i in range(7):
            a += 2
            b.append(a)
        print(b)
        for n in b:
            c += n
        print(c)


uzi = int(input('Zadejte liche cislo: '))

sou_lich(uzi)


