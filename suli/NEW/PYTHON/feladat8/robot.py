mozgas = input("Kérem a robot parancsait: ")
x = 0
y = 0
e = 0
d = 0
n = 0
k = 0
mozgas = mozgas.upper()
for i in mozgas:
    if i == "E":
        x+=1
        e+=1
    elif i == "D":
        x-=1
        d+=1
    elif i == "N":
        y-=1
        n+=1
    elif i == "K":
        y+=1
        k+=1
print(f"E betűk száma: {e}")
print(f"D betűk száma: {d}")
print(f"K betűk száma: {k}")
print(f"N betűk száma: {n}")
xlr = 0
xlrb = ""
ylr = 0
ylrb = ""
if x>=0:
    xlr += x
    xlrb = "E"
elif x<0:
    xlr += abs(x)
    xlrb = "D"
if x>=0:
    ylr += y
    ylrb = "K"
elif x<0:
    ylr += abs(y)
    ylrb = "N"
ywr = ""
xwr = ""
for i in range(xlr):
    xwr+=xlrb
for i in range(ylr):
    ywr+=ylrb
print(f"Egy legrövidebb út parancsszava: {ywr}{xwr}")