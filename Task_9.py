a, b, c = int(input('Введите три разных числа: ')), int(input()), int(input())
if a > b:
    if c > a:
        print('Среднее ', a)
    else:
        if c > b:
            print('Среднее ', c)
        else:
            print('Среднее ', b)
else:
    if c > b:
        print('Среднее ', b)
    else:
        if c > a:
            print('Среднее ', c)
        else:
            print('Среднее ', a)
