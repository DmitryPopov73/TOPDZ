print("Домашнее задание №5")
from random import randint
q = int(input("Введите длину массива: "))
z1 = int(input("Введите нижнее значение для генератора чисел: "))
z2 = int(input("Введите нижнее значение для генератора чисел: "))
x1 = [randint(z1,z2) for i in range(q)]
x2 = [randint(z1,z2) for i in range(q)]
print(f"Первый массив: {x1}")
print(f"Второй массив: {x2}")
x3 = []
for i in range (len(x1)):
    x3.append(x1[i])
for i in range (len(x2)):
    x3.append(x2[i])
print(f"Массив, содержащий элементы из двух списков: {x3}")
x4 = list(set(x3))
print(f"Массив, содержащий не повторяющиеся элементы из двух списков: {x4}")
x5 = []
for i in range (0,q):
    for j in range (0,q):
        if x1[i]==x2[j]:
            x5.append(x1[i])
x5 = list(set(x5))
print(f"Массив, содержащий общие элементы двух списков: {x5}")
x6 = [list(set(x1)),list(set(x2))]
print(f"Массив, содержащий уникальные элементы каждого из списков: {x6}")
x7 = [min(x1),max(x1),min(x2),max(x2)]
print(f"Массив, содержащий min-max первого и второго массивов: {x7}")