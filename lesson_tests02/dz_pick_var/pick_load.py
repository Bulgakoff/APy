import pickle

with open('favor.txt', 'rb') as f:
    res_load_ft = pickle.load(f)

print(res_load_ft)
print(type(res_load_ft))