import random, os




filestoopen = []

for root, dirs, files in os.walk("."):
    for file in files:
        filestoopen.append(os.path.join(root, file))


random.shuffle(filestoopen)

with open(filestoopen[0], 'r', errors='ignore') as f:
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
        link = f"/{word}"
        links.append(link)
    return links

if __name__ == '__main__':
    print(get_random_links())