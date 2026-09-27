a=input()
b=input()
if a=="красный" and b=="синий" or b=="красный" and a=="синий":
    print("фиолетовый")
elif a=="синий" and b=="желтый" or b=="синийжелтый" and a=="желтый":
    print("зеленый")
elif a=="красный" and b=="желтый" or b=="красный" and a=="желтый":
    print("оранжевый")
else:
    print("ошибка цвета")