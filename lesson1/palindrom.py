# Задача 8
# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
a = 'арозаупаланалапуазора'
с = 'арозауjаланалапуазора'
zz = ''.join(a)
print(f'-----zz {zz}')
z = list(reversed(zz))
print('/////////////')
print(f'-----z {z}')
z = ''.join(z)
print(f'z ============>>>>>>>{z}')
print(z==zz)


# qwe = a.split()
# print(qwe)
# разбить на буквы это 1 список
def del_list(arr):
    arr2d = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr2d.append(arr[i][j])
    return arr2d


res_del_list = del_list(a)
print(res_del_list)

# перевернуть слово
b = list(reversed(a))
print(b)


# сравнить оба списка
def equ(q, w):
    if a == b:
        print('lists equals each others')
    print('lists not equals each others')
    return a == b


res_equ = equ(a, b)
print(res_equ)


def equal_arr(e, r):
    for i in range(len(e)):
        if e[i] in r:
            print(f'{e[i]} равно ', end='')

        else:
            print(f' а  {e[i]} не равно ')


equal_arr(a, b)
