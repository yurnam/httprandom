import random, os

files = os.listdir(".")
filestoopen = []

for f in files:
    if os.path.isfile(f):
        filestoopen.append(f)

random.shuffle(filestoopen)

with open(filestoopen[-1], 'r') as f:
    data = f.read()


words = []

for word in data.split(','):
    word = word.strip().strip("'").strip('"')
    if word:
        words.append(word)




def get_random_links():
    random.shuffle(words)
    selected_words = words[:5]
    links = []
    for word in selected_words:
        word = word.strip()
        word = word.split('\n') [0]
        word = word.replace(' ', '/')
        link = f"/{word}"
        links.append(link)
    return links

if __name__ == '__main__':
    print(get_random_links())