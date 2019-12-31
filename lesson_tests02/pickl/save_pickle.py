
import pickle
person = {'name':'Bob', 'age':20}

with open('person.txt', 'wb') as f:
    pickle.dump(person, f)
print('объект записан')