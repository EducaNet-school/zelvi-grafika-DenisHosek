lit =[n for n in range(2, 1000) if all(n % m != 0 for m in range(2, n-1))]
lit_poc = []
pocet = int(input('Zadejte pocet prvo cisel: '))

for i in range(pocet):
    lit_poc.append(lit[i])

print(lit_poc)

#velmi originalni pouziti generatoru 