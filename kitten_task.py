# Задача:
# Введите два числа и выведите котиков
b, c = [int(i) for i in input('Введите два числа через пробел: ').split()]
a = []
print('Котики:')
for i in range(b):
    a.append([])
    for j in range(c):
        if (i + j) % 2 == 0:
            a[i].append('^')
        else:
            a[i].append('__')
for d in a:
    print(''.join(d))
