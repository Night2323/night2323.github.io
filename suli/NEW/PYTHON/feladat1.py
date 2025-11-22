print("-_-1. Feladat-_-")
#FFFFGGKKFFGKKUKGUUGGGKUUKGUGUFUGUF
def tev():
    print("Mozgásformák: \n - Úszás - U - 1km \n - Gyaloglás - G - 1km \n - Futás - F - 2km \n - Kerékpározás - K - 10km")
    aktivitas = input("Heti aktivitás: ")
    aktivitas = aktivitas.upper()
    for i in aktivitas:
        if i=="U" or i=="G" or i=="F" or i=="K":
            pass
        else:
            print("Érvénytelen formátum!")
            quit()
    return aktivitas
aktivitas = tev()

ossz = aktivitas.count("U")*1+aktivitas.count("G")*1+aktivitas.count("F")*2+aktivitas.count("K")*10

print("-_-2. Feladat-_-")
print(f"Az elért távolság: {ossz}")

print("-_-3. Feladat-_-")
if "U" in aktivitas and "G" in aktivitas and "F" in aktivitas and "K" in aktivitas:
    print("Bravó! Jutalma még 10 km")
    jut = 10
else:
    print("Nem jár jutalom")
    jut = 0

print("-_-4. Feladat-_-")
print(f"Eredménye: {jut+ossz}")
