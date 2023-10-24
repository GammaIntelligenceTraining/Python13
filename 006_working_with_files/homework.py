import string
with open('text_files/trimushketera.txt', 'r', encoding='utf8') as file:

    # book_text = file.read().replace(',', '').replace('!', '').replace('?', '').replace('.', '').lower()
    book_text = file.read()
    translation = str.maketrans('', '', string.punctuation)
    book_text = book_text.translate(translation)
    words = book_text.split()
    unique = list(set(words))
    unique.sort()

with open('text_files/tri_analysis.txt', 'w', encoding='utf8') as file:

    file.write(f'Total words: {len(words)}\n')
    file.write(f'Total unique words: {len(unique)}\n')
    for word in unique:
        file.write(word + '\n')
