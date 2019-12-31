word = 'слово'
print(len(word))
word1 = []
for i in range(len(word)):
    lett = word[i]
    letter = lett.upper() if i % 2 == 0 else lett.lower()
    word1.append(letter)
    result = ''.join(word1)
print(word1)
print(result)
