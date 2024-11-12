str1 = str(input("Введите строку: ")) # ввод строки
kolv = 0
for i in str1:
    if (i == "и"):
        kolv += 1
print("В строке ", kolv, "букв(-ы) и") # вывод результат цикла