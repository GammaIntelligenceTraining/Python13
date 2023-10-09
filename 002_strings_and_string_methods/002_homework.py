# Пользователь вводит имя и фамилию, в консоль выводится имя и фамилия с больщой буквы
# full_name = input('Please enter full name: ')
# print(full_name.title())


# Удалите все знаки препинания из строки
import string
sample = 'Hello, my name is Jack! I am from London - United Kingdom. Where are you from?'
# symbols = str.maketrans('', '', string.punctuation)
print(string.punctuation)
# print(type(string.punctuation))
# print(symbols)
# print(sample.translate(symbols))
print(sample.replace(',', '').replace('.', '').replace('?', '').replace('!', ''))

# Пользователь вводит произвольную строку, выведете её длину не учитывая пробелы
user_input = input('Enter something')
print(len(user_input.replace(' ', '')))


# Выведите в консоль строку с адресом '..\new_dir\tables.py'.
print('..\\new_dir\\tables.py')