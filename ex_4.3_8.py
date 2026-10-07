x=int(input())
if x==0:
    print("зеленый")
elif x==1 or x==3 or x==5 or x==7 or x==9:
    print("красный")
elif x==2 or x==4 or x==6 or x==8 or x==10:
    print("черный")
elif x== 12 or x==14 or x==16 or x==18 :
    print("красный")
elif x==11 or x==13 or x==15 or x==17:
    print("черный")
elif x==20 or x==22 or x==24 or x==26 or x==28:
    print("черный")
elif x==19 or x==21 or x==23 or x==25 or x==27:
    print("красный")
elif x==29 or x==31 or x==33 or x==35:
    print("черный")    
elif x==30 or x==32 or x==34 or x==36:
    print("красный")    
else:
    print("ошибка ввода")