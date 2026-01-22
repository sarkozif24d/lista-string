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

# 2. feladat# 2. feladat
mondat = "A programozás logikus gondolkodást fejleszt"
szavak = mondat.split()
hosszok = []

for szo in szavak:
    hosszok.append(len(szo))

print("Szóhosszak:", hosszok)

print("--------------------------------")


# 3. feladat
szam = input("Adj meg egy számot: ")
osszeg = 0

for karakter in szam:
    osszeg += int(karakter)

print("Számjegyek összege:", osszeg)

print("--------------------------------")

# 4. feladat
mondat2 = input("Írj be egy mondatot: ")

if mondat2.endswith("?"):
    print("Kérdő mondat")
elif mondat2.endswith("!"):
    print("Felszólító vagy óhajtó mondat")
else:
    print("Kijelentő mondat")

print("--------------------------------")

