f = open("/home/user/night2323.github.io/suli/NEW/PYTHON/feladat2/meres.txt")
szamok = f.read().strip("\n").split(", ")
idok = ["6:15","6:30","6:45", "7:00", "7:15", "7:30", "7:45", "8:00", "8:15", "8:30", "8:45", "9:00", "9:15", "9:30", "9:45", "10:00"]

print(len(szamok),len(idok))

for i in range(len(szamok)):
    szamok[i] = int(szamok[i])


print("\n2. feladat")

ossz = 0
for i in szamok:
    if i!=0:
        ossz = ossz+i
print(f"Összesen {ossz} kerékpárost számoltak.")

print("\n3. feladat\nÓránkénti mérések:")

for i in range(4):
    ossz = 0
    for o in range(4):
        n = i*4+o
        if szamok[n]>0:
            ossz = ossz+szamok[n]
    print(f"{i+6} órától {ossz} kerékpáros")
print("\n4. feladat")

print(f"Az áthaladók maximális száma: {max(szamok)}; a rögzítés időpontja: {idok[szamok.index(max(szamok))]}.")