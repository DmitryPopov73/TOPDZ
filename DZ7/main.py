print("Домашнее задание №7")
blockList = ["Леша", "Дима"]
guestList = []

while True:
    ch2 = True
    print(f"Меню:\n1 - Добавить гостя в список;\n2 - Удалить гостя из списка;\n3 - Просмотреть список гостей;\n4 - Просмотреть стоп список;\n5 - Выйти из программы.")
    ch1 = int(input(f"Ваш выбор: "))
    if ch1 == 1:
        while ch2 == True:
            ch3 = True
            if len(guestList)>=5 and len(guestList)<10:
                ch5 = int(input(f"Количество гостей уже {len(guestList)}!\n Вам нужны новые гости (1-Да, 2-Нет)? "))
                if ch5 == 1: 
                    pass
                elif ch5 == 2:
                    break
                else:
                    print("Неправильный ввод!")
                    break
            elif len(guestList) == 10:
                print(f"Количество гостей - 10. Хватит!")
                break
            guestName = input("Введите имя гостя для добавления в список приглашенных гостей: ")
            for i in range (0,len(blockList)):
                if guestName == blockList[i]:
                    print(f"Гость {guestName} в стоп списке!")
                    ch3 = False
            if ch3 == False:
                while True:
                    ch4 = int(input("Хотите ввести другое имя?\n1 - Да\n2 - Нет\nВаш выбор: "))
                    if ch4 == 1:
                        break
                    elif ch4 == 2:
                        print("Выход в основное меню!")
                        ch2 = False
                        break
                    else:
                        print("Неправильный ввод!")
            elif ch3 == True:
                guestList.append(guestName)
                ch2 = False        
    elif ch1 == 2:
        while True:
            ch6 = int(input("Вы хотите удалить гостя по имени (1) или по номеру (2)? "))
            if ch6 == 1:
                ch7 = True
                delUser = input("Введите имя, которое хотите удалить: ")
                for i in range (0,len(guestList)-1):
                    if guestList[i] == delUser:
                        guestList.pop(i)
                        ch7 = False
                        break
                if ch7 == True:
                    print("Мы не нашли такое имя!")
                break
            elif ch6 == 2:
                delUseri = int(input("Введите номер гостя для удаления: "))
                guestList.pop(delUseri-1)
                break
            else:
                print("Неправильный ввод!")
    elif ch1 == 3:
        guest = ""
        if len(guestList) == 0:
            print("В списке гостей никого нет!")
        else:
            for i in range (0,len(guestList)-1):
                guest += guestList[i] + ", "
            print(f"Список гостей в списке приглашенных: {guest}{guestList[len(guestList)-1]}.")
    elif ch1 == 4:
        block = ""
        for i in range (0,len(blockList)-1):
            block += blockList[i] + ", "
        print(f"Список гостей в стоп списке: {block}{blockList[len(blockList)-1]}.")
    elif ch1 == 5:
        print("Выход из программы!")
        break
    else:
        print("Неправильный ввод!")
