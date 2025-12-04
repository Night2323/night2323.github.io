f = open("/home/user/night2323.github.io/suli/NEW/PYTHON/feladat6/dobasok.txt")
dobasok = f.readline().split(", ")

print("\n2.feladat")
hely = 0
kiir = ""
letra = 0
for i in dobasok:
    if hely%10==0 and hely!=0:
        hely = hely-3
        letra = letra+1
    hely = hely+int(i)
    kiir = kiir+str(hely)+" "
print(kiir)

print("\n3.feladat")
print(f"A játék során {letra} alkalommal lépett létrára.")

print("\n4.feladat")
if hely>=45:
    print("A játékot befejezte.")
else:
    print("A játékot abbahagyta.")
