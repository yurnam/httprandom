import random, os


with open('data.txt', 'r') as f:
    data = f.read()


words = []

for word in data.split(','):
    word = word.strip().strip("'").strip('"')
    if word:
        words.append(word)



def get_random_words():
    random.shuffle(words)
    selected_words = words[:5]
    _words = []
    for _word in selected_words:
        _word = _word.strip()
        _word = _word.split('\n')[0]
        _words.append(word)
    return _words




def get_random_links():
    random.shuffle(words)
    selected_words = words[:5]
    links = []
    for w in selected_words:
        w = w.strip()
        w = w.split('\n') [0]
        w = w.replace(' ', '/')
        link = f"/{w}"
        links.append(link)
    return links

if __name__ == '__main__':
    print(get_random_links())
    print(get_random_words())