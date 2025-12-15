with open('data.txt', 'r') as f:
    data = f.read()


wors = []

for word in data.split(','):
    word = word.strip().strip("'").strip('"')
    if word:
        wors.append(word)

f2 = open('random_words_2.py', 'w')
f2.write(str(wors))