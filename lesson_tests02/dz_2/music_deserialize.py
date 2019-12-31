import json
import pickle

with open('group.json', 'r') as f:
    res_load_json = json.load(f)
print('loaded десериа json')
print(res_load_json)
print(type(res_load_json))


with open('group.txt', 'rb') as f:
    res_load_pickle = pickle.load(f)
print('loaded десериа pickle')
print(res_load_pickle)
print(type(res_load_pickle))