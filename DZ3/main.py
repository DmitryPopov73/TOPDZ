# print("Задача №1")
# check = ""
# age = int(input("Введите свой возраст: "))
# if age > 100:
#     print("Вам точно столько лет?")
#     check = input("1 - Да; 2 - Нет: ")
#     if check == "1":
#         if age >= 0 and age <= 11:
#             print("Вы ребенок!")
#         elif age >= 12 and age <= 17:
#             print("Вы подросток!")
#         elif age >=18 and age <= 59:
#             print("Вы взрослый!")
#         elif age >= 60:
#             print("Вы пенсионер!")
#         else:
#             print("Что-то пошло не так!")
#     elif check == "2":
#         print("Не балуйтесь!")
#     else:
#         ("Неправильный ввод!")
# else:
#     if age >= 0 and age <= 11:
#         print("Вы ребенок!")
#     elif age >= 12 and age <= 17:
#         print("Вы подросток!")
#     elif age >=18 and age <= 59:
#         print("Вы взрослый!")
#     elif age >= 60:
#         print("Вы пенсионер!")
#     else:
#         print("Что-то пошло не так!")

# print("Задача №2")
# i = int(input("Введите число от 0 до 9: "))
# if i == 0:
#     print("Нужный символ - <)>")
# elif i == 1:
#     print("Нужный символ - <!>")
# elif i == 2:
#     print("Нужный символ - <@>")
# elif i == 3:
#     print("Нужный символ - <#>")
# elif i == 4:
#     print("Нужный символ - <$>")
# elif i == 5:
#     print("Нужный символ - <%>")
# elif i == 6:
#     print("Нужный символ - <^>")
# elif i == 7:
#     print("Нужный символ - <&>")
# elif i == 8:
#     print("Нужный символ - <*>")
# elif i == 9:
#     print("Нужный символ - <(>")
# else:
#     print("Неправильный выбор!")
    
# print("Задача №3")
# x = int(input("Введите трехзначное число: "))
# if len(x) == 3:
#     print("В этом числе 3 цифры: ")
# else:
#     print("В этом числе не 3 цифры!")
# x1 = float(input("Введите первое число: "))
# x2 = float(input("Введите второе число: "))
# x3 = float(input("Введите третье число: "))
# x4 = len(str(x1).split(".")[1])
# x5 = len(str(x2).split(".")[1])
# x6 = len(str(x3).split(".")[1])
# x7 = x1 + x2 + x3
# x8 = x1 * x2 * x3
# x9 = max(x4,x5,x6)
# x10 = x4 + x5 + x6
# print(f"Что необходимо сделать с переменными?\n1 - сумма\n2 - произведение")
# check = int(input("Ваш выбор: "))
# if check == 1:
#     print(f"Сумма чисел: {round(x7,x9)}")
# elif check == 2:
#     print(f"Произведение чисел: {round(x8,x10)}")
# else:
#     print("Неправильный выбор!")
    
# print("Задача №2")
# a1 = float(input("Введите первое число: "))
# a2 = float(input("Введите второе число: "))
# a3 = float(input("Введите третье число: "))
# a4 = len(str(a1).split(".")[1])
# a5 = len(str(a2).split(".")[1])
# a6 = len(str(a3).split(".")[1])
# a7 = a4 + a5 + a6

# print(f"Что необходимо сделать с переменными?\n1 - вывести максимальное число\n2 - вывести минимальное число\n3 - вывести среднее арифметическое")
# check = int(input("Ваш выбор: "))
# if check == 1:
#     print(f"Максимальное число: {max(a1,a2,a3)}")
# elif check == 2:
#     print(f"Минимальное число: {min(a1,a2,a3)}")
# elif check == 3:
#     print(f"Среднее арифметическое: {round((a1+a2+a3)/3,a7+1)}")
# else:
#     print("Неправильный выбор!")

# print("Задача №3")

# b = float(input("Введите количество метров: "))
# b1 = b * 0.00062137
# b2 = b * 39.37
# b3 = b * 1.09361

# print(f"В какую единицу нужно перевести метры?\n1 - мили\n2 - дюймы\n3 - ярды")
# check = int(input("Ваш выбор: "))
# if check == 1:
#     print(f"В {round(b,6)} метрах: {round(b1,6)} миль")
# elif check == 2:
#     print(f"В {round(b,6)} метрах: {round(b2,6)} дюймов")
# elif check == 3:
#     print(f"В {round(b,6)} метрах: {round(b3,6)} ярдов")
# else:
#     print("Неправильный выбор!")