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
