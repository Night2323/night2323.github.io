txt = open("/home/user/night2323.github.io/suli/NEW/PYTHON/2023tavasz/3_Utemezes/taborok.txt","r")
eh = []
en = []
uh = []
un = []
tan = []
tab = []
for sor in txt:
    sor = sor.strip("\n")
    s = sor.split("\t")
    eh.append(s[0])
    en.append(s[1])
    uh.append(s[2])
    un.append(s[3])
    tan.append(s[4])
    tab.append(s[5])
txt.close()

print("2.feladat")
print("Az adatsorok száma:"+str(len(eh)))
print("Az először rögzített tábor témája: "+tab[0])
print("Az utolsó tábor témája: "+tab[-1])

print("3.feladat")
sz = 0
for i in tab:
    if i == "zenei":
        print("Zenei tábor kezdődik "+str(eh[sz])+". hó "+str(en[sz])+" napján")
    sz = sz+1

print("4.feladat")
x = "0"
for i in tan:
    if len(i) > len(x):
        x = i
print("Legnégszerűbbek:\n"+eh[tan.index(x)]+" "+en[tan.index(x)]+" "+tab[tan.index(x)])

def sorszam(ho,nap):
    if 6<=ho<=8:
        if 1>=nap>=31:
            print("Érvénytelen dátum")
        else:
            if ho==6 and 16<=nap<=30:
                n=nap-16
            elif ho==7 or ho==8:
                if ho==7:
                    n=14+nap
                else:
                    n=14+31+nap
            else:
                n=0  
    else:
        n=0
    return n

print("6.feladat")
ho2 = 6#int(input("Ho: "))
nap2 = 18#int(input("Nap: "))
c = 0
for i in range(len(eh)):
        ho = int(eh[i])
        nap = int(en[i])
        eleje = sorszam(ho,nap)
        ho = int(uh[i])
        nap = int(un[i])
        vege = sorszam(ho,nap)
        ho = int(ho2)
        nap = int(nap2)
        datum = sorszam(ho,nap)
        if datum>=eleje and datum<=vege:
            c = c+1
        print(eleje,vege)
print("Ekkor éppen "+str(c)+" tábor tart.")

print("7.feladat")
tanulo = input("Adja meg a tanuló betűjelét: ").upper()
f = open("/home/user/night2323.github.io/suli/NEW/PYTHON/2023tavasz/3_Utemezes/egytanulo.txt", "w")
mini=1000
maxi=0
napsz = 0
for i in range(len(eh)):
    if tanulo in tan[i]:
        f.write(eh[i]+"."+en[i]+"-"+uh[i]+"."+un[i]+". "+tab[i]+"\n")
        ho = int(eh[i])
        nap = int(en[i])
        eleje = sorszam(ho,nap)
        ho = int(uh[i])
        nap = int(un[i])
        vege = sorszam(ho,nap)
        if eleje<mini:
            mini=eleje
        if vege>maxi:
            maxi=vege
        napsz = napsz+(vege-eleje)
if (maxi-mini)<napsz:
    print("Nem mehet el mindegyik táborba.")
else:
    print("Elmehet mindegyik táborba.")
f.write
f.close()
