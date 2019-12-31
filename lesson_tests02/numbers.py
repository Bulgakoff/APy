# Задача 10
# Вы принимаете от пользователя последовательность чисел,
# разделённых запятой. Составьте список и кортеж с этими числами.
n = input('enter ').split()
print(n)


def order_num(arr):
    arr_int = [int(item) for item in arr]
    # for item in arr:
    #     item = int(item)
    #     arr_int.append(item)

    return arr_int


res_arr_int = order_num(n)

print(f'res_order_num= list=={res_arr_int}')
# print(f'res_order_num==tuple={}')
# /////////////////////////////////////////////////
res_arr_int = tuple(res_arr_int)
print(res_arr_int)

# def order_num(arr):
#     turpl = ()
#     # arr_int = [int(item) for item in arr]
#     for item in arr:
#         item = int(item)
#
#
#     return arr_int
#
#
# res_arr_int = order_num(res_arr_int)