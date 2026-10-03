a1=input()
a2=input()
a3=input()
b1=len(a1)
b2=len(a2)
b3=len(a3)
if b1 < b2 and b1 < b3:
    print(a1)
elif b2 < b1 and b2 < b3:
     print(a2)
elif b3 < b1 and b3 < b2:
     print(a3)

if b1 > b2 and b1 > b3:
    print(a1)
elif b2 > b1 and b2 > b3:
     print(a2)
elif b3 > b1 and b3 > b2:
     print(a3)