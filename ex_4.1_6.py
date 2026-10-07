d=int(input()) 
c=d%10        #еденицы
b=(d//10)%10  #десятки
a=(d//100)%10 #сотни
y=d//1000     #тысячи
if y+c==a-b:
    print("ДА")
else:
    print("НЕТ")


