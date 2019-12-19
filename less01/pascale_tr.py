# Задача 7
# Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике
# на вершине и по бокам стоят единицы, а каждое число внутри равно
# сумме двух расположенных над ним чисел.
def ent_zero(i, j):
    arr_2d = []
    for arr in range(i):
        internal_arr = []
        for arr_in in range(j):
            internal_arr.append(1)
        arr_2d.append(internal_arr)
    return arr_2d


result = ent_zero(5, 5)
print(result)

def matrix_print(res):
    for i in range(len(res)):
        for j in range(len(res[i])):
            print(res[i][j], end=' ')
        print()


matrix_print(result)
print('//////////////////////////////////////////')


    # for i in range(1, 5):
    #     for j in range(1, 5):
    #        result[i][j] = result[i-1][j] + result[i-1][j-1]


# def matrix_print2(res):
#     for i in range(res):
#         for j in range(len(i)):
#             print(res[i][j], end=' ')
#         print()
#
#
# matrix_print2(result)


# def matrix_print(res):
#     for i in range(len(res)):
#         for j in range(i+1):
#             print(res[i][j], end=' ')
#         print()
#

# matrix_print(result)