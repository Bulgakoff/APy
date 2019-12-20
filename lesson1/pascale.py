print('////////////////# create 2 size list and  fillfull////////////////////')


def p_m(arrr):
    for i in range(len(arrr)):
        for j in range(len(arrr[i])):
            print(arrr[i][j], end=' ')
        print()


def create_2d(n, m):
    arr_2d = []
    for p in range(n):  # ндекс внешнего цикла
        internal = []
        for w in range(m):
            internal.append(1)
        arr_2d.append(internal)
    return arr_2d


res_arr = create_2d(5, 5)
print(f'-----res_arr = {res_arr}')
print('//////////////////rewrite 0 or 1 ///////////////////')


def rewrite_0or1(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr[i])):
            arr[i][j] = 0
    return arr


res_rewrite = rewrite_0or1(res_arr)
print(f' res_rewrite =  {res_rewrite}')

print('//////////////////calc_triangle_pascale///////////////////')


def triangle_pas(ar):
    for i in range(1, len(ar)):
        for j in range(1, len(ar[i])):
            ar[i][j] = ar[i - 1][j] + ar[i - 1][j - 1]  #
    return ar  # [[1, 4, 10, 20, 35], [1, 4, 10, 20, 35], [1, 4, 10, 20, 35], [1, 4, 10, 20, 35], [1, 4, 10, 20, 35]]


res_triangle_pas = triangle_pas(res_rewrite)
print(f'res_triangle_pas = {res_triangle_pas}')
# /////////////////////////////////////////////////
p_m(res_arr)
print()
p_m(res_rewrite)
