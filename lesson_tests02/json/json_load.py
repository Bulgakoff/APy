
import json

with open('fr.txt', 'r') as f:
    res_friend_read = json.load(f)
print(type(res_friend_read))
print(res_friend_read)
print('прочтено')