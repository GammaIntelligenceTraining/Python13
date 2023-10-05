'''
Написать программу которая:
	1. Высчитывает возраст из заданых данных (current_year - нынешний год, year_of_birth - год рождения)
	2. Найти недостающую часть кода (code_2)
		a. найдите остаток от x деленого на y
		b. полученый результ умножте на 13
		c. извлеките квадратный корень из полученного результата
		d. возьмите целую часть от результа
	3. Соединить код в отдельную переменную
	    пример:
	        475-12-967
	4. Вывести строку:
		пример:
			Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.
'''

# years
current_year = 2023
year_of_birth = 1988
# code parts
code_1 = '354'
code_3 = 132
# name
user_name = 'John'
user_surname = 'Smith'
# code 2 data
x = 152
y = 132

age = current_year - year_of_birth

# step_1 = x % y
# step_2 = step_1 * 13
# step_3 = step_2 ** 0.5
# step_4 = int(step_3)
# code_2 = str(step_4)

code_2 = str(int((x % y * 13) ** 0.5))

code = code_1 + '-' + code_2 + '-' + str(code_3)

# Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.
print('Hello ' + user_name + ' ' + user_surname + '. You are ' +
      str(age) + ' years old. Your secret code is ' + code + '.')