# print("Программа №1")
# x1 = int(input("Введите начало диапазона: "))
# x2 = int(input("Введите конец диапазона: "))
# for i in range(x1,x2+1):
#     if i%7 == 0:
#         print(f"Число {i} делится на 7")

# print("Программа №2")
# x1 = int(input("Введите начало диапазона: "))
# x2 = int(input("Введите конец диапазона: "))
# allch = ""
# allchub = ""
# kr7 = ""
# kr5 = 0
# for i in range (x1,x2):
#     allch +=f"{i}, "
# print(f"Все числа диапазона: {allch}{x2}.")
# for i in range (x1,x2+1):
#     if i%7 == 0:
#         kr7 += f"{i}, "
#     if i%5 == 0:
#         kr5 += 1
# while x2 > x1:
#     allchub +=f"{x2}, "
#     x2 -= 1
# print(f"Все числа диапазона в убывающем порядке: {allchub}{x1}.")
# print(f"Все числа кратные 7: {kr7}")
# print(f"Количество чисел, кратных 5: {kr5}")

# print("Программа №3")
# x1 = int(input("Введите начало диапазона: "))
# x2 = int(input("Введите конец диапазона: "))
# for i in range (x1,x2+1):
#     if i%3 == 0 and i%5 == 0:
#         print("Fizz Buzz")
#     elif i%5 == 0:
#         print("Buzz")
#     elif i%3 == 0: 
#         print("Fizz")
#     else:
#         print(f"{i}")