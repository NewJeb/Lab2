f1 = 1
f2 = 1
n = int(input("Введите число: "))
if n >= 1000:
 print("Фибоначчи: ")
 print('f1:', f1)
 print('f2:', f2)
 while n > 2:
     f1, f2 = f2, f1 + f2
     print('-', f2)
     n = n - 1
else:
     print("Введите 4х значное число!")