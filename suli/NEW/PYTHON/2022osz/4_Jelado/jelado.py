from math import *

fi = open("/home/user/night2323.github.io/suli/NEW/PYTHON/2022osz/4_Jelado/jel.txt")
jelek = []
for i in fi:
    i = i.strip("\n")
    jelek.append(i)

print("2. feladat")

#ssz = int(input("Jel sorszáma:"))-1
ssz = 1
print(jelek[ssz].split(" ")[3], jelek[ssz].split(" ")[4])

def eltelt(i1,i2):
    i1 = i1[0]*3600+i1[1]*60+i1[2]
    i2 = i2[0]*3600+i2[1]*60+i2[2]
    diff = i2-i1
    return diff

print("\n4. feladat")

i1 = [int(jelek[0].split(" ")[0]),int(jelek[0].split(" ")[1]),int(jelek[0].split(" ")[2])]
i2 = [int(jelek[-1].split(" ")[0]),int(jelek[-1].split(" ")[1]),int(jelek[-1].split(" ")[2])]

diff = eltelt(i1,i2)
ora=diff//3600
perc=(diff-(ora*3600))//60
mp = (diff-(ora*3600)-(perc*60))
print(f"Időtartam: {ora}:{perc}:{mp}")

print("\n5. feladat")
min1 = 99999990
min2 = 99999990
max1 = 0
max2 = 0
for i in jelek:
    temp = i.split(" ")
    if int(temp[3])<min1:
        min1 = int(temp[3])
    if int(temp[4])<min2:
        min2 = int(temp[4])

    if int(temp[3])>max1:
        max1 = int(temp[3])
    if int(temp[4])>max2:
        max2 = int(temp[4])
print(f"Bal alsó: {min1} {min2}, jobb felső: {max1} {max2}")


print("\n6. feladat")
ossz = 0
for i in range(len(jelek)-1):
    temp = jelek[i].split(" ")
    temp2 = jelek[i+1].split(" ")
    ossz = ossz + sqrt(((int(temp[3])-int(temp2[3]))**2)+((int(temp[4])-int(temp2[4]))**2))
ossz = round(ossz, 3)
print(f"Elmozdulás: {ossz} egység")

print("\n\n")

fo = open("/home/user/night2323.github.io/suli/NEW/PYTHON/2022osz/4_Jelado/kimarad.txt", "w")

for i in range(len(jelek)-1):
    pr = "0"
    x = 0
    y = 0
    ido = 0
    ko = 0
    pr = 0
    t = ""
    temp = jelek[i].split(" ")
    temp2 = jelek[i+1].split(" ")
    i1 = [int(temp[0]),int(temp[1]),int(temp[2])]
    i2 = [int(temp2[0]),int(temp2[1]),int(temp2[2])]
    diff = eltelt(i1,i2)
    
    if diff>(300):
        ido = (diff//300)-1
    
    if abs(int(temp2[3])-int(temp[3]))>10:
        x = (abs(int(temp2[3])-int(temp[3])))//10
    
    if abs(int(temp2[4])-int(temp[4]))>10:
        y = (abs(int(temp2[4])-int(temp[4])))//10
    
    if x>y:
        ko = x
    elif x<y:
        ko = y
    
    if ido>ko:
        pr = ido
        t = "időeltérés"
    elif ko>ido:
        pr = ko
        t = "koordináta-eltérés"

    if pr!=0:
        fo.write(f"{i2[0]} {i2[1]} {i2[2]} {t} {pr}\n")
    
fo.close()
