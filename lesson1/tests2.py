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
print('//////////////пока наша сумма < 10/////')
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
print('//////////////тонкость while огда всегда True нужно ежеодно условие/////')
a = [1, 2.4, 4.5, 6, 6, 67, 6]
dd = []
i = 0
sum3 = 0
while len(a) > i and a[i] > 0:
    sum3 = sum3 + a[i]
    dd.append(sum3)
    i += 1
print(sum3)
print(dd)
print('/////////////дз    /////')

qwe = [1, 2.4, 4.5, 5, 6, -67, -6, -5, -6, -4]
qwerty = list(reversed(qwe))
print(qwerty)
s4 = 0
i = 0
while qwerty[i] < 0 and i < len(qwerty):
    s4 += qwerty[i]
    i += 1
print(s4)

for p in range(qwe[len(qwe) - 1], qwe[0], -1):  # 1й аргум - старт, 2й аргум - cтоп (не включая),
    # 3й аргум - шаг просмотра (перехода (инкркментации<здесь декрементатции>)),
    s4 += p
print(s4)

print('///////////for /for /for /for ///тонкость while огда всегда True нужно ежеодно условие/////')

names = ['Non', 'Vov', 'Coc', 'Xox', 'Dod']
for i, item in enumerate(names):
    if names[i] == 'Non':
        print(f'-- {item} ' * 3)
    elif names[i] == 'Coc':
        print(f'-- {item} ' * 3)
print('///////////ложенные циклы begine/////')

for item in names:
    print(item, end=' ')
print()

for i in range(len(names)):
    print(names[i], end=' ')
print('///////////ложенные циклы2/////\n')

for i in range(len(names)):
    for j in range(i + 1):  # ange показывает диапазон итераций - повторений
        print(names[i])

print('///////////enumarate это круто /////\n')

for i, item in enumerate(names):
    for j in range(i):
        print(item)
        print(f'-----{j}', end=' ')

print('///////////enumarate это круто /////\n')
names = ['Non', 6, 6, 67, 6, 'Vov', 6, 'Coc', 6, 67, 6]

d = {}
z = None
for item in names:
    if type(item) == str:
        d[item] = []
        z = item
    else:
        d[z].append(item)
print(d)

print('///////////кол слов в списке  в списке  списке через словарь/////\n')
lik = 'кол слов в списке  в списке  списке через словарь'
qwe = lik.split()
result = {i: qwe.count(i) for i in qwe}
print(result)
result = [k for k, v in result.items() if v == max(result.values())]
print(result)
# ////////////////////////////////////////////
print('/////////////////////////////////////')
lik = 'кол слов в списке  в списке  списке через словарь'
qwe = lik.split()

asd = {}
temp = 0
for p in qwe:
    asd[p] = []
    temp = qwe.count(p)
    asd[p].append(temp)

print(asd)
print('////////////////////lhдругой вариант/////////////////')
lik = 'кол слов в списке  в списке  списке через словарь'
qwe = lik.split()

asd = {}
temp = 0
for p in qwe:
    if p in asd:
        asd[p] = asd[p] + 1
    else:
        asd[p] = 1
print(asd)

print('////////////////////lhдругой вариант/////get(... , ...)/////////////////')

lik = 'кол слов в списке  в списке  списке через словарь'
qwe = lik.split()

asd = {}
temp = 0
for p in qwe:
    asd[p] = asd.get(p, 0) + 1
print(f'================================================={asd}')
print('///////////////////списк списков////////////////')


def arr_2d(m, n):
    arr_2d = []
    for i in range(m):
        print()
        inter_arr = []
        for j in range(n):
            inter_arr.append(0)

    return arr_2d


print(arr_2d(4, 4))
