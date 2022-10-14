import random
slovnik = ['',"jedna", "dva", "tri", "ctiry", "pet", "set", "sedm", "osm", "devet", "deset", "jedenact", "dvanact", "trinact", "ctrnact", "patnact", "sestnact", "sedmnact", "osumnact","devatenact", "dvacet", "tricet", "ctyricet", "padesat", "sedesat", "sedumdesat", "osumdesat","devadesat"]

cisla = round(random.uniform(0,99))

if cisla <=19:
    print(slovnik[cisla])
elif cisla >=20 and cisla <= 29:
    cisla -= 20
    print(slovnik[20], slovnik[cisla])
elif cisla >=30 and cisla <= 39:
    cisla -= 30
    print(slovnik[21], slovnik[cisla])
elif cisla >=40 and cisla <= 49:
    cisla -= 40
    print(slovnik[22], slovnik[cisla])
elif cisla >=50 and cisla <= 59:
    cisla -= 50
    print(slovnik[23], slovnik[cisla])
elif cisla >=60 and cisla <= 69:
    cisla -= 60
    print(slovnik[24], slovnik[cisla])
elif cisla >=70 and cisla <= 79:
    cisla -= 70
    print(slovnik[25], slovnik[cisla])
elif cisla >=80 and cisla <= 89:
    cisla -= 80
    print(slovnik[26], slovnik[cisla])
elif cisla >=90 and cisla <= 99:
    cisla -= 90
    print(slovnik[27], slovnik[cisla])


  