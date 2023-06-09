print("Задача №1")
x1 = float(input("Введите первое число: "))
x2 = float(input("Введите второе число: "))
x3 = float(input("Введите третье число: "))
x4 = len(str(x1).split(".")[1])
x5 = len(str(x2).split(".")[1])
x6 = len(str(x3).split(".")[1])
x7 = x1 + x2 + x3
x8 = x1 * x2 * x3
x9 = max(x4,x5,x6)
x10 = x4 + x5 + x6
print(f"Сумма чисел: {round(x7,x9)}\nПроизведение чисел: {round(x8,x10)}")

print("Задача №2")
a1 = int(input("Введите зарплату за месяц в рублях: "))
a2 = int(input("Введите сумму ежемесячного платежа по кредиту в банке в рублях: "))
a3 = int(input("Введите задолженность за коммунальные услуги на начало месяца в рублях: "))
a4 = a1 - a2 - a3
print(f"Сумма, оставшаяся после всех выплат: {a4}")

print("Задача №3")
b1 = float(input("Введите длину первой диагонали в мм: "))
b2 = float(input("Введите длину второй диагонали в мм: "))
b3 = len(str(b1).split(".")[1])
b4 = len(str(b2).split(".")[1])
s = (b1 * b2) / 2
print(f"При длинах диагоналей равных {b1} и {b2} мм - площадь ромба равна: {round(s,(b3+b4+1))} мм")

print("Задача №4")
print("To be\nor not\nto be")

print("Задача №5")
print(f"“Life is what happens\n\twhen\n\t\tyou’re busy making other plans”\n\t\t\t\t\t John Lennon.")