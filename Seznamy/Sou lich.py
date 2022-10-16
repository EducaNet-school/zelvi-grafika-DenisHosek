uzi = int(input('Zadejte liche cislo: '))


if (uzi % 2) == 0:
   uzi += 1 
   #OK, chces vyrobit liche cislo, lepsi je varovat uyzivatele
   #je to drobnost
   x = uzi + 2 #tohle bych vyhodil
x = uzi + 2
for i in range(8):
    uzi += x
    x = uzi + 2

print(uzi)

#Denisi, na tohle jeste mrkni, napocitava to vice nez ma
#jeste jsem udelal 2 drobne poznamky vyse