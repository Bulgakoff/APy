import json

ft = [{'name': 'Вечнвая любовь', 'artist': 'Агата Кристи'}, {'name': 'Вечная смерть', 'artist': 'Жопа'}]
with open('tracks.txt', 'w', encoding='utf-8') as f:
    json.dump(ft, f)
print('записанооооооооо!')
