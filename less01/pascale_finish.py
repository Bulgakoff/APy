# Задача 7
# Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике
# на вершине и по бокам стоят единицы, а каждое число внутри равно
# сумме двух расположенных над ним чисел.
def add_arr(n, m):
    arr_2d = []
    for arr in range(n + 1):
        internal = []
        for j in range(m + 1):
            internal.append(1)
        arr_2d.append(internal)
    return arr_2d


res_add_arr = add_arr(10, 10)
print(f'res_add_arr==={res_add_arr}')


# //////////////////////////////////////////////
def only_col1(arr):
    for i in range(len(arr)):  # i индеск снаружи
        for j in range(1, len(arr[i])):  # j индеск внутри
            arr[i][j] = 0
    return arr


res_only_col1 = only_col1(res_add_arr)
print(f'res_only_col1==={res_only_col1}')


# ///////////////////////////////////////////////
def calc_pascale(arr):  # просто переписывается
    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    return arr


res_calc_pascale = calc_pascale(res_only_col1)
print(f'res_calc_pascale==={res_calc_pascale}')


# ////////////////////////////////////////////////
def pri_matr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()


pri_matr(res_calc_pascale)

