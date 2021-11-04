
n = int(input("Введите количество слагаемых: "))
n = n - 1
v = 1
l = 3
for b in range(n):
 if b % 2 == 0:
            v = v - 1 / l
else:
            v = v + 1 / l
l += 2
v = v * 4
print('Результат дес. число:',v)
print('Результат дес. число:',int(v))