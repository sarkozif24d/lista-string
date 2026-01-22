import random

# 1. feladat
lista = []

for i in range(10):
    lista.append(random.randint(0,9))

print("Lista:", lista)

paratlan = 0
for szam in lista:
    if szam % 2 == 1:
        paratlan += 1

print("Páratlan számok száma:", paratlan)

# ismétlődések eltávolítása
uj_lista = []
for szam in lista:
    if szam not in uj_lista:
        uj_lista.append(szam)

print("Ismétlődés nélkül:", uj_lista)

# hiányzó számok 0-9
hianyzo = []
for i in range(10):
    if i not in lista:
        hianyzo.append(i)

if len(hianyzo) == 0:
    print("Minden szám szerepel 0-9 között")
else:
    print("Hiányzó számok:", hianyzo)

print("--------------------------------")