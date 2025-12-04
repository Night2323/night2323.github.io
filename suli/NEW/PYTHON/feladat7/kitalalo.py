import random

szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]
m = random.randrange(0,14)
rejtett = szavak[m]
valasz = ""
eddig = [".",".",".",".",".","."]
darab = 0
while valasz!="stop":
    darab += 1
    valasz = input("Kérem a tippet: ")
    if valasz != "stop" and len(valasz)==6:
        eddig2 = ""
        for i in range(6):
            if valasz[i]==rejtett[i]:
                eddig[i] = valasz[i]
        for i in eddig:
            eddig2 += i
        if eddig2==rejtett:
            print(f"{darab} tippeléssel sikerült kitalálni.")
            quit()
        print(f"Az eredmény: {eddig2}")
    else:
        quit()
    