# открываем файл для записи бфйтов
# with open('tesss.txt', 'bw') as f:
#     # пишем строку байт
#     str = 'Привет мир'
#     f.write(str.encode('utf - 8'))
# print(str.encode('utf - 8'))

with open('tesss.txt', 'w', encoding='utf - 8') as f:# либо так либо выше
    # пишем строку байт
    str = 'Привет мир'
    f.write(str)
print(str.encode('utf - 8'))

# читаем как текст С КОДИРОВКОЙ 'utf - 8'
with open('tesss.txt', 'rb') as f:
    # print(f.read())
    result = f.read()  # елаем копию
    print(result)
    print(type(result))
    strin = result.decode('utf-8')
    print(strin)
