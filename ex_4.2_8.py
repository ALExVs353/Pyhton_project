stolb1=int(input())
sroka1=int(input())
stolb2=int(input())
sroka2=int(input())
if (stolb1==stolb2 or stolb1+1==stolb2 or stolb1-1==stolb2) and (sroka1==sroka2 or sroka1+1==sroka2 or sroka1-1==sroka2):
    print("YES")
else:
    print("NO")