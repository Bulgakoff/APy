word = 'слово'
print(len(word))
word1 = []
for i in range(len(word)):
    lett = word[i]
    letter = lett.upper() if i % 2 == 0 else lett.lower()
    word1.append(letter)
    result = ''.join(word1)
print(word1)
print(result)
# //////////////////////////////////////////////////////////////////
# создать список квадрратов чисел
num = [1, 2, 3, 4, 3, 4, 5, 7, 4]
num1 = [p ** 2 for p in num]
print(num1)

# список име на букву А
names = ['Фывпу', 'Аррпок', 'Щдаоар', 'Алло']
names1 = [p for p in names if 'А' in p]

print(names1)
a = [1, 2, 3]
b = a[:]
print(b)
# /////////////////////////////
import random

n = random.randint(2, 5)
print(n)
a = 10
b = 0
try:
    if n == 4:
        print('gggggggggggggg')
except ValueError:
    print('hfhfhhfhfhhfhfhjfjjjjjjjjjjjjjjj')


def pr(nnn):
    return nnn


res_pr = pr(n)
pr(res_pr)

# 4. Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13,
# функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.
import random

n = random.randint(5, 8)


def numbers(nn):
    if nn == 8:
        raise ValueError(f'Mistaken {nn}')
    else:
        return nn ** 2


try:
    res_numbers = numbers(n)
except ValueError as a:
    print(a)
else:
    print(res_numbers)