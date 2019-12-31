import json
import pickle

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
               {'name': 'Шапито', 'year': 2014}]}
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)
print('аписано сериа json')

with open('group.txt', 'wb') as f:
    pickle.dump(my_favourite_group, f)
print('аписано сериа pickle')
