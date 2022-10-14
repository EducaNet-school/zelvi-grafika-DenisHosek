seznam = [10, 90, 20, 80, 30, 40, 70, 60]

n = float(input("Zadejte cislo"))

for a in seznam:
    if a > n:
        print(a)
    else: 
        print('Nepravdive tvrzeni')
