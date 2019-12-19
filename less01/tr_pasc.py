n = int(input('введите колличество уровней, строк :   '))  # вводим колличество уровней которые надо


# расчитать, а это на 1 меньше тут работает формула определениия
# элемента a[i][j] = a[i-1][j] + a[i-1][j-1](исключаем первый столбец с 1 и строку )


# заполним его начальными значения\ми (проинициализировать)
def full_tab(nn):
    triangle = []  # наш список внешний
    for i in range(nn):
        triangle.append([1] + [0] * nn)
    # for i in triangle:
    #     print(i)
    return triangle


res_triangle = full_tab(n)
print(f'=====triangle {res_triangle}')


def rewrite_triangle(arr, nn):
    for i in range(1, nn):  # перезапись матрицы
        for j in range(1, nn):
            arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
    return arr


res_arr = rewrite_triangle(res_triangle, n)
print(f' >>>>>>>>{res_arr}')


def pr_triangle(arr, nn):
    for i in range(0, nn):  # печать всех элементов индекс уже с 0 ...
        for j in range(0, nn):
            print(arr[i][j], end=" ")
        print()


pr_triangle(res_triangle, n)
