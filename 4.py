from math import cos, factorial, radians
x = radians(float(input("Введите значение ∠ ")))
n = int(input("Введите число: "))
cos = sum(
    pow(-1, i) * pow(x, 2 * i) / factorial(2 * i) for i in range(n))
print("Вывод (cos)  %s:" % cos)