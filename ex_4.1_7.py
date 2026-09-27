a=int(input())
b=int(input())
c=int(input())
if a>0<b>0<c:
    print(a+b+c)
if a>0>b<0<c:
    print(a+c)
if a<0<b>0<c:
    print(b+c)
if a>0<b>0>c:
    print(a+b)
if a>0>b<0>c:
    print(a)
if a<0<b>0>c:
    print(b)
if a<0>b<0<c:
    print(c)
if a<0>b<0>c:
    print("0")