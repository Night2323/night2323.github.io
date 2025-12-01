l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

if len(l1)!=len(l2):
    if (len(l1)-len(l2))>0:
        for i in range(len(l1)-len(l2)):
            l2.append(0)
    else:
        for i in range(len(l2)-len(l1)):
            l1.append(0)

ou = []
ou.append(l1[0]+l2[0])
for i in range(len(l1)):
    if i==0:
            pass
    else:
        if ou[i-1]>9:
            ou.append(l1[i]+l2[i]+1)
            ou[i-1] = ou[i-1]-10
if ou[-1]>9:
    ou[-1] = ou[-1]-10
    ou.append(1)
print(ou)
