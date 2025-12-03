import random
a = 0
p = 0
fdszm = int(input("Hány alkalommal legyen feldobás: "))
for i in range(fdszm):
    v1 = random.randrange(1,6)
    v2 = random.randrange(1,6)
    v3 = random.randrange(1,6)
    if (v1+v2+v3)<10:
        print(f"Dobás: {v1} + {v2} + {v3} = {v1+v2+v3} \t Nyert: Anni")
        a+=1
    
    else:
        print(f"Dobás: {v1} + {v2} + {v3} = {v1+v2+v3} \t Nyert: Panni")
        p+=1

print(f"A háték során {a} alkalommal Anni, {p} alkalommal Panni nyert.") 