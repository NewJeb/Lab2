import math

a = float(input("Введите переменную a: "))
b = float(input("Введите переменную b: "))
c = float(input("Введите переменную c: "))

D = b**2 - 4*a*c
print('Дискриминант =', D)
if D < 0 or D == 0:
    print('Дискриминант меньше 0 или равен 0, корей нет!')
else:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print('x1 =', x1)
    print('x1 =', x2)