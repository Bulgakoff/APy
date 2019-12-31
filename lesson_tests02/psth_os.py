import os

npath = os.getcwd()
print(npath)

s = 'hello string'
sb = b'hello bites'
for item in sb:
    print(item, end=' ')
print()
print(s[:4])
print(sb[:4])

sbite = s.encode('utf-8')
print(sbite)
print(type(sbite))
sbite_tostr =sbite.decode('utf -8')
print(sbite_tostr)