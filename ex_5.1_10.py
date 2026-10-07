srednee=0
a=int(input())
b=a%10
d=(a//10)%10
c=a//100
I=max(b,c,d)-min(b,c,d)
srednee=b+c+d-max(b,c,d)-min(b,c,d)
if I==srednee:
    print("Число интересное")
else:
    print("Число неинтересное")