a = int(input('Введите целое число от 1 до 100: '))
if 0 >= a or a > 100:
    print('Число от 1 до 100!')
    while 0 >= a or a > 100:
        a = int(input('Введите целое число от 1 до 100: '))
if a % 10 >= 2 and a % 10 <= 4 and a / 10 != 1:
    print(a, 'года')
elif a % 10 == 1 and a / 10 != 1:
    print(a, 'год')
else:
    print(a, 'лет')