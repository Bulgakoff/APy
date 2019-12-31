import json

with open('tracks.txt', 'r') as f:
    res_json = json.load(f)
print(res_json)
print(type(res_json))
print('выгрузили')