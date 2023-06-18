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
# if len(str(x)) == 3:
#     if list(str(x))[0] == list(str(x))[1]:
#         print(f"Первая цифра <{list(str(x))[0]}> равна второй цифре <{list(str(x))[1]}>")
#     elif list(str(x))[2] == list(str(x))[1]:
#         print(f"Вторая цифра <{list(str(x))[1]}> равна третьей цифре <{list(str(x))[2]}>")
#     elif list(str(x))[0] == list(str(x))[2]:
#         print(f"Первая цифра <{list(str(x))[0]}> равна третьей цифре <{list(str(x))[2]}>")
#     else:
#         print(f"Первая цифра <{list(str(x))[0]}> не равна второй цифре <{list(str(x))[1]}> и не равна третьей цифре <{list(str(x))[2]}>")
# else:
#     print("В этом числе не 3 цифры!")

# print("Задача №4")

# x = int(input("Введите год для проверки: "))
# if x&4 != 0 or (x%100 == 0 and x%400 !=0):
#     print(f"Год <{x}> не високосный!")
# else:
#     print(f"Год <{x}> високосный!")

# print("Задача №5")
# x = int(input("Введите пятизначное число: "))
# if len(str(x)) == 5:
#     if list(str(x))[0] == list(str(x))[4] and list(str(x))[1] == list(str(x))[3]:
#         print(f"Число {x} - палиндром")
#     else:
#         print(f"Число {x} - не палиндром")
# else:
#     print(f"Число {x} - не пятизначное")

# print("Задача №6")
# print(f"Курс доллара на сегодня:\n1 USD = 0,91 EUR\n1 USD = 36,9 UAN\n1 USD = 1,7 AZN")
# usd = float(input("Введите количество долларов USD: "))
# choice = input("В какую валюту перевести ваши доллары?: ")
# if choice == "EUR":
#     result = usd * 0.91
#     print(f"{usd} долларов = {round(result,5)} евро")
# elif choice == "UAN":
#     result = usd * 36.9
#     print(f"{usd} долларов = {round(result,5)} гривен")
# elif choice == "AZN":
#     result = usd * 1.7
#     print(f"{usd} долларов = {round(result,5)} манат")
# else:
#     print("Неправильный ввод!")
    
# print("Задача №7")
# x = float(input("Введите сумму покупки: "))
# if x < 200:
#     y = x
# elif 200 <= x < 300:
#     y = 0.97 * x
# elif 300 <= x < 500:
#     y = 0.95 * x
# elif x >= 500:
#     y = 0.93 * x
# else:
#     pass
# print(f"Ваша сумма покупки с учетом скидки: {y}")

# print("Задача №8")
# dlokr = float(input("Введите длину окружности: "))
# perkr = float(input("Введите периметр квадрата: "))
# if dlokr/3.14 <= perkr/4:
#     print("Окружность помещается в квадрат!")
# else:
#     print("Окружность не помещается в квадрат!")

# print("Задача №9")
# qs = 0
# q1 = int(input("В каком году Европейский Союз впервые ввел евро в качестве валюты?\n1 - 1995 год\n2 - 1999 год\n3 - 2005 год\nВаш ответ: "))
# if q1 == 2:
#     print("Ваш ответ правильный!")
#     qs += 2
# elif q1 in {1,3}:
#     print("Ваш ответ неправильный!")
# else:
#     print("Вы ввели неправильное значение")
# q2 = int(input("Сколько полос на флаге США?\n1 - 11\n2 - 12\n3 - 13\nВаш ответ: "))
# if q2 == 3:
#     print("Ваш ответ правильный!")
#     qs += 2
# elif q2 in {1,2}:
#     print("Ваш ответ неправильный!")
# else:
#     print("Вы ввели неправильное значение")
# q3 = int(input("В 1952 году президентом какой страны был предложен Альберт Эйнштейн?\n1 - США\n2 - Израиль\n3 - Великобритания\nВаш ответ: "))
# if q3 == 2:
#     print("Ваш ответ правильный!")
#     qs += 2
# elif q2 in {1,3}:
#     print("Ваш ответ неправильный!")
# else:
#     print("Вы ввели неправильное значение")
# print(f"Количество набранных баллов: {qs}")

# print("Задача №10")
# x1 = ""
# x2 = ""
# x3 = ""
# x = input("Введите дату в формате ДД.ММ.ГГГГ без незначащих нулей (первое января первого года - 1.1.1): ")
# if int(x.split(".")[2])&4 != 0 or (int(x.split(".")[2])%100 == 0 and int(x.split(".")[2])%400 !=0):
#     y = 1 # Год не високосный
# else:
#     y = 2 # Год високосный



# if x.split(".")[1] == "1" and x.split(".")[0] == "31":
#     x1 = "1"
#     x2 = "2"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "3" and x.split(".")[0] == "31":
#     x1 = "1"
#     x2 = "4"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "5" and x.split(".")[0] == "31":
#     x1 = "1"
#     x2 = "6"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "7" and x.split(".")[0] == "31":
#     x1 = "1"
#     x2 = "8"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "8" and x.split(".")[0] == "31":
#     x1 = "1"
#     x2 = "9"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "10" and x.split(".")[0] == "31":
#     x1 = "1"
#     x2 = "11"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "12" and x.split(".")[0] == "31":
#     x1 = "1"
#     x2 = "1"
#     x3 = str(int(x.split(".")[2])+1)
# elif x.split(".")[1] == "4" and x.split(".")[0] == "30":
#     x1 = "1"
#     x2 = "5"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "6" and x.split(".")[0] == "30":
#     x1 = "1"
#     x2 = "7"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "9" and x.split(".")[0] == "30":
#     x1 = "1"
#     x2 = "10"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "11" and x.split(".")[0] == "30":
#     x1 = "1"
#     x2 = "12"
#     x3 = x.split(".")[2]
# elif x.split(".")[1] == "2" and x.split(".")[0] == "28":
#     if y == 1:
#         x1 = "1"
#         x2 = "3"
#         x3 = x.split(".")[2]
#     elif y == 2:
#         x1 = "29"
#         x2 = "2"
#         x3 = x.split(".")[2]
# elif x.split(".")[1] == "2" and x.split(".")[0] == "29":
#     x1 = "1"
#     x2 = "3"
#     x3 = x.split(".")[2]
# else:
#     x1 = str(int(x.split(".")[0])+1)
#     x2 = x.split(".")[1]
#     x3 = x.split(".")[2]
# print(f"Следующая дата: {x1}.{x2}.{x3}")