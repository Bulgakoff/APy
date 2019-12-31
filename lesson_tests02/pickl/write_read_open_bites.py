# открываем файл для записи бфйтов
with open('tesss2.txt', 'bw') as f:
    # пишем строку байт
    str = 'Привет мир'
    f.write(str.encode('utf - 8'))
# print(str.encode('utf - 8'))

# читаем как текст С КОДИРОВКОЙ 'utf - 8'
with open('tesss2.txt', 'r', encoding='utf -8') as f:
    print(f.read())
