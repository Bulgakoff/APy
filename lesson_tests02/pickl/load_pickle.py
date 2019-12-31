
import pickle

with open('person.txt', 'rb') as f:
    result_person = pickle.load(f)
print(result_person)