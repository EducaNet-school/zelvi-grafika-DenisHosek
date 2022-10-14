seznam = ["Franta", "Marek", "Marysa", "Pepa", "Ondra"]
o = "1"
while o == "1":
    print("1. Pridani jmena")
    print("2. Vypis seznamu")
    print("3. Odebrani ze seznamu")
    print("4. Pocet jmen")
    print("5. Serazeni jmen")
    o = input("Vyberte moznost")

    if o == "1":
        seznam.append(input("Jmeno"))
        print(seznam)
        print("1. pokracovat")
        print("2. ukoncit")
        o = input("Vyberte moznost")
    elif o == "2":
           print(seznam)
           print("1. pokracovat")
           print("2. ukoncit")
           o = input("Vyberte moznost")
    elif o == "3":
        seznam.remove(input("Odeberte jmeno"))
        print(seznam)
        print("1. pokracovat")
        print("2. ukoncit")
        o = input("Vyberte moznost")
    elif o == "4":
        pocet = len(seznam)
        print("Pocet", pocet)
        print("1. pokracovat")
        print("2. ukoncit")
        o = input("Vyberte moznost")
    elif o == "5":
        seznam.sort()
        print(seznam)
        print("1. pokracovat")
        print("2. ukoncit")
        o = input("Vyberte moznost")
    else: 
        print("Tuto moznost neznam")
        print("Opakujte akci znovu")
        print("1. pokracovat")
        print("2. ukoncit")
        o = input("Vyberte moznost")
