# -------------------------------------------------------------------------------------------------
#                                            ЗАДАЧА №1
# -------------------------------------------------------------------------------------------------



# print("Задача №1")
# userList = []
# while True:
#     imyaUser = input("Введите имя пользователя: ")
#     famUser = input("Введите фамилию пользователя: ")
#     dateUser = input("Введите дату рождения DD.MM.YYYY (без нулей!):")
#     if int(dateUser.split(".")[1]) == 6:
#         if int(dateUser.split(".")[0]) <= 13:
#             vozrUser = 2023 - int(dateUser.split(".")[2])
#         else:
#             vozrUser = 2023 - int(dateUser.split(".")[2]) - 1
#     elif int(dateUser.split(".")[1]) < 6:
#         vozrUser = 2023 - int(dateUser.split(".")[2])
#     else:
#         vozrUser = 2023 - int(dateUser.split(".")[1]) - 1
#     yearUser = int(dateUser.split(".")[2])
#     infoUser = {
#         "imyaUser" : imyaUser,
#         "famUser" : famUser,
#         "vozrUser": vozrUser,
#         "yearUser": yearUser,
#         }
#     userList.append(infoUser)
# # print(infoUser)
#     break
# print(f"Имя: {userList[0]['imyaUser']}, Фамилия: {userList[0]['famUser']}, Возраст: {userList[0]['vozrUser']}, Год рождения: {userList[0]['yearUser']}")



# -------------------------------------------------------------------------------------------------
#                                            ЗАДАЧА №2
# -------------------------------------------------------------------------------------------------



# print("Задача №2")
# put = int(input("Выберите путь 1 - 3: "))
# if put == 1:
#     print("Речка спятила с ума —\nПо домам пошла сама.")
#     otvet = input("Ваш ответ: ")
#     if otvet == "водопровод":
#         print("Ваш ответ верный!")
#     else:
#         print("Ваш ответ неверный!")
# elif put == 2:
#     print("Музыкант, певец, рассказчик —\nА всего труба да ящик.")
#     otvet = input("Ваш ответ: ")
#     if otvet == "граммофон":
#         print("Ваш ответ верный!")
#     else:
#         print("Ваш ответ неверный!")
# elif put == 3:
#     print("На раскрашенных страницах\nМного праздников хранится.")
#     otvet = input("Ваш ответ: ")
#     if otvet == "календарь":
#         print("Ваш ответ верный!")
#     else:
#         print("Ваш ответ неверный!")
# else:
#     print("Неправильный выбор!")



# -------------------------------------------------------------------------------------------------
#                                            ЗАДАЧА №3
# -------------------------------------------------------------------------------------------------

# print("Задача №3")
# import random

'''
Задаем границы диапазона с помощью переменных x1, x2. Переменная x3 - рандомная из диапазона x1, x2. Переменная j - счётчик количества попыток. Выводим x3 для проверки!
'''

# x1 = int(input("Задайте нижнюю границу диапазона: "))
# x2 = int(input("Задайте верхнюю границу диапазона: "))
# x3 = int(random.randint(x1, x2))
# j = 0
# print(f"Загадонное число - {x3}!")

'''
Задаем цикл while для возможности вводить варианты ответа, пока не угадаем.
При каждой попытке переменная j увеличивается на 1. x4 - переменная варианта ответа. Далее идут проверки: на попадание в диапазон, число больше или меньше загаданного числа
или мы угадали. Как только угадали - цикл завершается.
'''

# while True:
#     j = j+1
#     print("Компьютер загадал число из диапазона. Теперь вам нужно его угадать!")
#     x4 = int(input("Введите ваш вариант ответа:"))
#     if x4<x1 or x4>x2:
#         print("Вы ввели число не из диапазона!")
#     elif x4<x3:
#         print("Ваше число меньше загаданного!")
#     elif x4>x3:
#         print("Ваше число больше загаданного!")
#     elif x3==x4:
#         print("Вы угадали!")
#         break

'''
Вывод количества попыток
'''

# print(f"Вы сделали {j} попыток!")



# -------------------------------------------------------------------------------------------------
#                                            ЗАДАЧА №4
# -------------------------------------------------------------------------------------------------



# print("Задача №4")


# '''
# Создаем пустой массив
# '''

# raspisan = [[
# {
#     "numUrok" : "1",
#     "nameUrok" : "Алхимия",
#     "time1Urok" : "8.00",
#     "time2Urok" : "10.15",
# }
# ,
# {
#     "numUrok" : "2",
#     "nameUrok" : "Математика",
#     "time1Urok" : "10.20",
#     "time2Urok" : "11.25"
# }
# ,
# {
#     "numUrok" : "3",
#     "nameUrok" : "Физика",
#     "time1Urok" : "11.30",
#     "time2Urok" : "12.25"
# }
# ,
# {
#     "numUrok" : "4",
#     "nameUrok" : "Математика",
#     "time1Urok" : "13.00 ",
#     "time2Urok" : "14.00"
# }
# ]
# ,
# [
# {
#     "numUrok" : "1",
#     "nameUrok" : "Математика",
#     "time1Urok" : "8.00",
#     "time2Urok" : "10.15",
# }
# ,
# {
#     "numUrok" : "2",
#     "nameUrok" : "Алхимия",
#     "time1Urok" : "10.20",
#     "time2Urok" : "11.25"
# }
# ,
# {
#     "numUrok" : "3",
#     "nameUrok" : "Математика",
#     "time1Urok" : "11.30",
#     "time2Urok" : "12.25"
# }
# ,
# {
#     "numUrok" : "4",
#     "nameUrok" : "Физика",
#     "time1Urok" : "13.00 ",
#     "time2Urok" : "14.00"
# }
# ]]

# while True:
#     x = int(input("На какой день выдать расписание (0 - пн, 1 - вт)? : "))
#     if x != 0 and x != 1:
#         print("Ошибка выбора!")
#     else:
#         for i in range (0,4):
#             print(f"{raspisan[x][i]['numUrok']}. {raspisan[x][i]['nameUrok']} {raspisan[x][i]['time1Urok']} - {raspisan[x][i]['time2Urok']}")

# print("Задача №5")
# userList = []
# ch1 = True
# while ch1 == True:
#     print(f"Меню:\n1 - зарегистрировать пользователя\n2 - посмотреть список зарегестрированных пользователей\n3 - войти в программу\n4 - выйти из программы")
#     check1 = int(input("Ваш выбор: "))
#     if check1 == 1:
#         while True:
#             imUser = input("Введите имя нового пользователя: ")
#             famUser = input("Введите фамилию нового пользователя: ")
#             logUser = input("Введите логин нового пользователя: ")
#             ch3 = 1
#             while ch3 == 1:
#                 if len(userList) > 0:
#                     for i in range (0,len(userList)):
#                         if logUser == userList[i]['logUser']:
#                             while True:
#                                 print("Такой логин уже существует!")
#                                 check3 = int(input("Ввести другой логин для этого пользователя (1 - Да, 2 - Выйти в основное меню): "))
#                                 if check3 == 1:
#                                     logUser = input("Введите логин нового пользователя: ")
#                                     break
#                                 elif check3 == 2:   
#                                     print("Выйти в основное меню!")
#                                     ch3 = 3
#                                     break
#                                 else:
#                                     print("Неправильный выбор!")
#                     if ch3 == 3:
#                         ch3 == 3
#                     else:
#                         ch3 = 2
#                 else: ch3 = 2
#             if ch3 == 3:
#                 break
#             passUser = input("Введите пароль нового пользователя: ")
#             infoUser = {
#                 "imUser" : imUser,
#                 "famUser" : famUser,
#                 "logUser": logUser,
#                 "passUser": passUser,
#             }
#             ch2 = True
#             while ch2 == True:
#                 check2 = int(input(f"Зарегистрировать пользователя(1  -Да; 2 - Нет)?: "))
#                 if check2 == 1:
#                     userList.append(infoUser)
#                     print("Пользователь зарегистрирован!")
#                     ch2 = False
#                 elif check2 == 2:
#                     print("Пользователь не зарегистрирован!")
#                     ch2 = False
#                 else:
#                     print("Неправильный выбор!")
#             break
#     elif check1 == 2:
#         if len(userList) == 0:
#             print("Нет зарегестрированных пользователей!")
#         else:
#             for i in range (0,len(userList)):
#                 print(f"Пользователь №{i+1}:\nИмя: {userList[i]['imUser']}\nФамилия: {userList[i]['famUser']}\nЛогин: {userList[i]['logUser']}")
#     elif check1 == 3:
#         if len(userList) == 0:
#             print("Нет зарегестрированных пользователей!")
#         else:
#             ch4 = True
#             j = 0
#             while ch4 == True:
#                 login = input("Введите логин: ")
#                 for i in range (0, len(userList)):
#                     if userList[i]['logUser'] == login:
#                         j = i+1
#                 if j == 0:
#                     print("Логин не существует!")
#                     while True:
#                         check4 = int(input("Повторить ввод логина (1 - Да, 2 - Выйти в основное меню)?: "))
#                         if check4 == 1:
#                             ch4 = True
#                             break
#                         elif check4 == 2:
#                             ch4 = False
#                             break
#                         else:
#                             print("Неправильный ввод!")
#                 else:
#                     ch5 = True
#                     while ch5 == True:
#                         password = input("Введите пароль: ")
#                         if userList[j-1]['passUser'] != password:
#                             print("Пароль неправильный!")
#                             while True:
#                                 check5 = int(input("Повторить ввод пароля (1 - Да; 2 - Вернуться к вводу логина; 3 - Выйти в основное меню)?: "))
#                                 if check5 == 1:
#                                     ch5 = True
#                                     break
#                                 elif check5 == 2: 
#                                     ch5 = False
#                                     break
#                                 elif check5 == 3:
#                                     ch5 = False
#                                     ch4 = False
#                                     break
#                                 else:
#                                     print("Неправильный ввод!")
#                         else:
#                             print("Вы вошли в программу!")
#                             ch6 = True
#                             while ch6 == True:
#                                 print(f"Меню:\n1 - посмотреть информацию об аккаунте\n2 - редактировать данные своего аккаунта\n3 - выйти в основное меню")
#                                 check6 = int(input("Ваш выбор: "))
#                                 if check6 == 1:
#                                     print(f"Данные Вашего аккаунта:\nЛогин: {userList[j-1]['logUser']}\nИмя: {userList[j-1]['imUser']}\nФамилия: {userList[j-1]['famUser']}")
#                                 elif check6 == 2:
#                                     while True:
#                                         print(f"Меню:\n1 - редактировать имя\n2 - редактировать фамилию\n3 - редактировать пароль\n4 - выйти в меню")
#                                         check7 = int(input("Ваш выбор: "))
#                                         if check7 == 1:
#                                             userList[j-1]['imUser'] = input("Введите новое имя пользователя: ")
#                                             print(f"Ваше новое имя пользователя - {userList[j-1]['imUser']}")
#                                         elif check7 == 2:
#                                             userList[j-1]['famUser'] = input("Введите новую фамилию пользователя: ")
#                                             print(f"Ваша новая фамилия пользователя - {userList[j-1]['famUser']}")
#                                         elif check7 == 3:
#                                             userList[j-1]['passUser'] = input("Введите новый пароль пользователя: ")
#                                             print(f"Ваш новый пароль пользователя - {userList[j-1]['passUser']}")
#                                         elif check7 == 4:
#                                             print("Выход в главное меню!")
#                                             break
#                                         else:
#                                             print("Неправильный ввод!")
#                                 elif check6 == 3:   
#                                     ch6 = False
#                                 else:
#                                     print("Неправильный ввод!")
#                             ch5 = False
#                             ch4 = False
#     elif check1 == 4:
#         print("Выход из программы!")
#         ch1 = False
#     else:
#         print("Неправильный выбор!")