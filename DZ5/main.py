print("Создание персонажа:")
ch1 = True
while ch1 == True:
    ch2 = True
    regGender = int(input(f"Введите пол персонажа:\n1 - Мужской\n2 - Женский\nВаш выбор: "))
    if regGender == 1:
        gender = "Мужской"
    elif regGender == 2:
        gender = "Женский"
    else:
        print("Неправильный ввод!")
    if regGender == 1 or regGender == 2:
        while ch2 == True:
            ch3 = True
            regRace = int(input(f"Введите расу персонажа:\n1 - Человек\n2 - Эльф\n3 - Орк\n4 - Вернуться к выбору пола\nВаш выбор: "))
            if regRace == 1:
                race = "Человек"
            elif regRace == 2:
                race = "Эльф"
            elif regRace == 3:
                race = "Орк"
            elif regRace == 4:
                ch2 = False
            else:
                print("Неправильный ввод!")
            if regRace == 1 or regRace == 2 or regRace == 3:
                while ch3 == True:
                    ch4 = True
                    if regRace == 1:
                        regRole = int(input(f"Введите роль персонажа:\n1 - Воин\n2 - Лучник\n3 - Вернуться к выбору расы\nВаш выбор: "))
                        if regRole == 1:
                            role = "Воин"
                        elif regRole == 2:
                            role = "Лучник"
                        elif regRole == 3:
                            ch3 = False
                        else:
                            print("Неправильный ввод!")
                    elif regRace == 2:
                        regRole = int(input(f"Введите роль персонажа:\n1 - Воин\n2 - Маг\n3 - Вернуться к выбору расы\nВаш выбор: "))
                        if regRole == 1:
                            role = "Воин"
                        elif regRole == 2:
                            role = "Маг"
                        elif regRole == 3:
                            ch3 = False
                        else:
                            print("Неправильный ввод!")
                    elif regRace == 3:
                        regRole = int(input(f"Введите роль персонажа:\n1 - Воин\n2 - Шаман\n3 - Вернуться к выбору расы\nВаш выбор: "))
                        if regRole == 1:
                            role = "Воин"
                        elif regRole == 2:
                            role = "Шаман"
                        elif regRole == 3:
                            ch3 = False
                        else:
                            print("Неправильный ввод!")
                    if regRole == 1 or regRole == 2:
                        while ch4 == True:
                            ch5 = True
                            regName = input(f"Введите своё имя или <Выйти>: ")
                            if regName == "Выйти":
                                ch4 = False
                            else:
                                while ch5 == True:
                                    ch6 = True
                                    regPers = int(input(f"Зарегистрировать персонажа (1 - Да, 2 - Нет):"))
                                    if regPers == 1:
                                        print(f"Ваш персонаж зарегистрирован!\nПол: {gender}\nРаса: {race}\nРоль: {role}\nИмя персонажа: {regName}")
                                        ch1 = False
                                        ch2 = False
                                        ch3 = False
                                        ch4 = False
                                        ch5 = False
                                        ch6 = False
                                    elif regPers == 2:
                                        while ch6 == True:
                                            reg = int(input("На какой этап вернуться?\nИмя - 1\nРоль - 2\nРаса - 3\nПол - 4\nВыйти из программы - 5\nВаш выбор: "))
                                            if reg == 1:
                                                print("Возвращаемся на этап ввода имени!")
                                                ch5 = False
                                                ch6 = False
                                            elif reg == 2:
                                                print("Возвращаемся на этап ввода роли!")
                                                ch4 = False
                                                ch5 = False
                                                ch6 = False
                                            elif reg == 3:
                                                print("Возвращаемся на этап ввода расы!")
                                                ch3 = False
                                                ch4 = False
                                                ch5 = False
                                                ch6 = False
                                            elif reg == 4:
                                                print("Возвращаемся на этап ввода пола!")
                                                ch2 = False
                                                ch3 = False
                                                ch4 = False
                                                ch5 = False
                                                ch6 = False
                                            elif reg == 5:
                                                print("Выход из программы!")
                                                ch1 = False
                                                ch2 = False
                                                ch3 = False
                                                ch4 = False
                                                ch5 = False
                                                ch6 = False
                                            else:
                                                print("Неправильный ввод!")