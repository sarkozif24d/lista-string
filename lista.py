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

# 5. feladat
szamok = []

while True:
    adat = input("Adj meg egy számot (stop a vége): ")
    if adat == "stop":
        break
    else:
        szamok.append(int(adat))

print("Beolvasott számok száma:", len(szamok))

if len(szamok) > 0:
    legnagyobb = max(szamok)
    legkisebb = min(szamok)
    print("Különbség:", legnagyobb - legkisebb)

    oszthato3 = []
    for sz in szamok:
        if sz % 3 == 0:
            oszthato3.append(sz)

    print("3-al osztható számok:", oszthato3)
else:
    print("Nem lett szám megadva")