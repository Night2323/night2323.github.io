f = open("/home/user/night2323.github.io/suli/NEW/PYTHON/feladat4/tomeg.txt")
adatok = f.read().strip("\n").split(", ")
for i in range(len(adatok)):
    adatok[i] = int(adatok[i])

print("\n2. feladat")

ossz = 0
for i in adatok:
    ossz = ossz+i
print(f"A tárgyak tömegének összege: {ossz} kg")

print("\n3. feladat")

dobozok = []
current = 0
for i in adatok:
    print(current,i)
    if current+i>20:
        dobozok.append(current)
        current = 0
        current = current+i
    else:
        current = current+i
dobozok.append(current)
print(f"A dobozok tartalmának tömege (kg): {' '.join(map(str, dobozok))}")
print(f"A szükséges dobozok száma: {len(dobozok)}")
    