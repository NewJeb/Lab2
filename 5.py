n = int(input('Напишите число N: '))
k=0
for x in range(n):
    if(x** 3 > n):
        break
    for y in range(n):
        if(y** 3 + x** 3 > n):
            break
        for z in range(n):
            if(y** 3 + x** 3 + z** 3 > n):
                break
            if((x** 3)+(y** 3)+(z** 3) == n):
                print('-' ,x, y, z)
                k += 1
if(k==0):
    print('No such combinations')