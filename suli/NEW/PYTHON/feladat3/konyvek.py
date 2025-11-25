ev = []
qrt = []
szar = []
nevcim = []
kiad = []

f = open("/home/user/night2323.github.io/suli/NEW/PYTHON/feladat3/kiadas.txt","r")
for i in f:
    i = i.split(";")
    ev.append(int(i[0]))
    qrt.append(int(i[1]))
    szar.append(i[2])
    nevcim.append(i[3])
    kiad.append(int(i[4]))


print("2. feladat")
nev = input("Szerző:")
nev = nev.split(" ")
cnt = 0
for i in range(len(nevcim)):
    if nev[0] in nevcim[i] and nev[1] in nevcim[i]:
        cnt = cnt+1
if cnt!=0:
    print(f"{cnt} könyvkiadás")
else:
    print("Nincs könyvkiadás")

print("3. feladat")
cnt = 0
for i in kiad:
    if i==max(kiad):
        cnt = cnt+1
print(f"Legnagyobb példányszám {max(kiad)}, előfordult {cnt} alkalommal")

print("4. feladat")
i = 0
megvan = False
while megvan==False:
    if kiad[i]>=40000 and szar[i]=="kf":
        megvan = True
    else:
        i = i+1
print(f"{ev[i]}/{qrt[i]} {nevcim[i]}")

print("5. feladat")
print("Év   Magyar kiadás   Magyar példányszám  Küldöldi kiadás Küldöldi példányszám")
for i in range(4):
    macnt = 0
    mapld = 0
    kfcnt = 0
    kfpld = 0
    for o in range(len(ev)):
        if 2020+i==ev[o]:
            if szar[o]=="ma":
                macnt = macnt+1
                mapld = mapld+kiad[o]
            elif szar[o]=="kf":
                kfcnt = kfcnt+1
                kfpld = kfpld+kiad[o]
    print(f"{2020+i}        {macnt}                 {mapld}         {kfcnt}                 {kfpld}")

print("6. feladat")
dupla = []
dnagy = []
for i in nevcim:
    if nevcim.count(i) > 2:
        if i not in dupla:
            dupla.append(i)
            if kiad[nevcim.index(i)]<kiad[nevcim.index(i,nevcim.index(i)+1)] and kiad[nevcim.index(i)]<kiad[nevcim.index(i,nevcim.index(i,nevcim.index(i)+1)+1)]:
                dnagy.append(i)
print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek:")
for i in dnagy:
    print(i)      
    