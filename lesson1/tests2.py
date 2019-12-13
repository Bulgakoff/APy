def func(n, k):
    d = []
    if n > 20:
        return 0
    else:
        sum_t = 0

        for i in range(1, n):
            if i % 2 == 0:
                sum_t = sum_t + i ** k
                d.append(sum_t)
        return sum_t, d


result = func(10, 2)
print(result)
print('///////////////////while//////////////////////')


def funca(n, k):
    d = []
    if n > 20:
        return 0
    else:
        sum_t = 0
        i = 1

        while i < n:
            if i % 2 == 0:
                sum_t = sum_t + i ** k
                d.append(sum_t)
            i += 1
        return sum_t, d


result = funca(10, 2)
print(result)

print('//////////////while когда размер  списока не определен//////////////')
a = [1, 2.4, 4.5, 6, 6, 67, 6, -5, -6, -7, -7, -2]
i = 0
su = 0
while a[i] > 0:
    su = su + a[i]
    i += 1  # пребор проходит инкрементацией i += 1

print(su)
print('//////////////for //for i, item in enumerate(a)////////////')
sum1 = 0
q = []
for i, item in enumerate(a):
    if item <= 0:
        break  # жрет память ---- что  бы этого не было добавим break и условие/
    else:
        sum1 = sum1 + item
        q.append(sum1)
print(a)
print(sum1, q)

print('//////////////for///////жрет память тк идет до конца  что  бы этого не было добавим break и условие/////')
sum2 = 0
for p in a:
    if p <= 0:  # что  бы этого не было добавим break и условие/
        break
    else:
        sum2 += p
print(f'......>>>>>{sum2}')
print('//////////////gjrfока наша мумма Ю10/////')
a = [1, 2.4, 4.5, 6, 6, 67, 6, -5, -6, -7, -7, -2]
dd = []
i = 0
sum3 = 0
while a[i] > 0 and sum3 < 10:
    sum3 = sum3 + a[i]
    dd.append(sum3)
    i += 1
print(sum3)
print(dd)
