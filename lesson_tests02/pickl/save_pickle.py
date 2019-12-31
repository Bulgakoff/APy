import pickle

person = {'name': 'Bob', 'age': 20}

with open('person.txt', 'wb') as f:
    res_pic_dump = pickle.dump(person, f)
print(type(res_pic_dump))# не тип смысла выносить в переменную нет
print('объект записан')
