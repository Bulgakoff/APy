qqq = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def swap(q, w, e):
    temp = q[e]
    q[e] = q[w]
    q[w] = temp


def mirror2(q):
    for arr in q:
        for j in range(len(arr) // 2):  # число иттераций сколько раз два крайинх элемента
            # меняются местами в иттерации arr внешенгог цикла q
            swap(arr, j, len(arr) - 1 - j)  # в вызове индексы

    return q


result2 = mirror2(qqq)
print(f'result2 =-----temp ------def swap(q, w, e):-----------{result2}')


def pri_matrix(mirror_tab):
    for i in range(len(mirror_tab)):
        for j in range(len(mirror_tab[i])):
            print(mirror_tab[i][j], end=' ')
        print('топор')


pri_matrix(result2)
