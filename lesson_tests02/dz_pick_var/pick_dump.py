
import pickle
ft = [{'name': 'Вечнвая любовь', 'artist': 'Агата Кристи'}, {'name': 'Вечная смерть', 'artist': 'Жопа'}]

with open('favor.txt', 'wb') as f:
    res_dump_ft = pickle.dump(ft, f)
print(res_dump_ft)
print('сериализовали ')