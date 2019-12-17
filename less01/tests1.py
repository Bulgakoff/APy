#
# area(a,b)
# is_even()
# 1 миля = 1.609 километров (км)
miles = 50
km = miles * 1.6
print('////////////////# 1 convert:////////////////')


def convert(m):
    km = m * 1.6
    return km


km = convert(miles)
print(km)
print('////////////////# 2 is_even:////////////////')


# s=a*b
def area(a, b):
    s = a * b
    return s


s = area(4, 6)
print(s)
print('////////////////# 3 is_even:////////////////')


def is_even(n):
    return n % 2 == 0


q = is_even(33)
print(q)

print('////////////////# 3 temp////////////////')
qwe = ['hello', 'good', 'bad']
temp = qwe[2]
qwe[2] = qwe[0]
qwe[0] = temp
print(qwe)
qwe[0], qwe[2] = qwe[2], qwe[0]
print(qwe)
print('////////////////#4 total_sum////////////////')
total_sum = 0
qwe = [1, 2, 3, 5, 5]
for e in qwe:
    total_sum += e
    print(total_sum, end=' , ')

print('////////////////#4 total_sum////////////////')
q = [1, 2, 34, -4, 5, -5, 6, -6, -1]
sum1 = 0
e = []
for w in q:
    if w < 0:
        sum1 += w
        e.append(w)
print(e)
print(f'-------{sum1}')
print('////////////////#4 negativ enumatrate///////////////')


def sum_deff(arr):
    arr_new = []
    sum2 = 0
    for i, item in enumerate(arr):
        if item < 0:
            sum2 = sum2 + item
            arr_new.append(item)
    return f'-массив --{arr_new}-- сумма -{sum2}'

    # print(arr_new)
    # print(f'>>>>>enumerate {sum2}')


res = sum_deff(q)
print(f'>>>>>enumerate {res}')

qwe = ['fyf', 'gjgj', 'erw', 'ooiuyt', 'stop', 'hjcd', 'vzxz', 'rew']
i = 0
qw = []
while qwe[i] != 'stop':
    qw.append(qwe[i])
    i += 1
print(qw)

print('////////////////#4 negativ range///////////////')

qwer = []
for i in range(len(qwe)):
    if qwe[i] == "stop":
        break
    qwer.append(qwe[i])
print(qwer)

print('////////////////задача 1 перевод в словарь списка///////////////')
qwe = ['fir', 1, 2, 3, 'sec', 56, 67, 78, 'fouth', -54, -60]


def m_dic(my_list):
    my_dict = {}
    curr_key = None
    for p in my_list:
        if type(p) == str:
            my_dict[p] = []
            curr_key = p
        else:
            my_dict[curr_key].append(p)

    return my_dict


res = m_dic(qwe)
print(res)
print('////////////////задача 2 перевод в словарь списка///////////////')
qwe = 'задача задача задача задача задача задача перевод в словарь списка  перевод в словарь словарь словарь словарь '
qwer = qwe.split()
print(qwer)
my_dict = {i: qwer.count(i) for i in qwer}
res_max_key = [k for k, v in my_dict.items() if v == max(my_dict.values())]
print(f'>>>>>>>>>>>>-----------{res_max_key}')
print(qwer)
res_max_key_w = ['no' if 'задча' not in qwer else k for k, v in my_dict.items() if v == max(my_dict.values())]
print(f'============================={res_max_key_w}')

print(my_dict)
# ////////////////////////////////////////
qwe = 'задача задача задача задача задача задача перевод в словарь списка  перевод в словарь словарь словарь словарь '
qwer = qwe.split()
aaa = {}
for p in qwer:
    if p not in aaa:
        aaa[p] = 1
    else:
        aaa[p] = aaa[p] + 1
print(f'-----------==if p not in aaa:========+++++++{aaa}')
# /////////////////////////////////////////////////////////////////
aaa = {}
for p in qwer:
    aaa[p] = aaa.get(p, 0) + 1
print(f'-----------==aaa.get(p, 0)========+++++++{aaa}')
# ////////////////////////////////////////////////
qwe = 'задача задача задача задача задача задача перевод в словарь списка  перевод в словарь словарь словарь словарь '
qwer = qwe.split()
aaa = {}
for p in qwer:
    res = qwer.count(p)
    aaa[p] = res
print(f'--------qwer.count(p)------------{aaa}')

# //////////////////////////////////////////////////////////

qqq = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
qwe = [1, 2, 3]


def swap(q, w, e):
    temp = q[e]
    q[e] = q[w]
    q[w] = temp


def mirror1(q):
    www = []
    for p in q:
        p.reverse()
        www.append(p)
    return www


result = mirror1(qqq)
print(f'---in --buffer--www = []---------{result}-')


# /////////////////////////////////////////
def mirror2(q):
    for arr in q:
        for j in range(len(arr) // 2):  # число иттераций сколько раз два крайинх элемента
            # меняются местами в иттерации arr внешенгог цикла q
            swap(arr, j, len(arr) - 1 - j)  # в вызове индексы

    return q


result2 = mirror2(qqq)
print(f'-----temp = q[i][len(i)-1]-----------{result2}')


# /////////////////////////////////////////////////
def pri_matrix(mirror_tab):
    for i in range(len(mirror_tab)):
        for j in range(len(mirror_tab[i])):
            print(mirror_tab[i][j], end=' ')
        print('топор')


pri_matrix(mirror1(result))
