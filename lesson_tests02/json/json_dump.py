import json

friend = [{'name': 'Bob', 'age': 20}, {'ph': [1547, 23444]}]
# friend_json = json.dumps(friend)
# print(friend_json)
# print(type(friend_json))

with open('fr.txt', 'w') as f:
    res_friend = json.dump(friend, f)
print(type(res_friend))
print('записано')
