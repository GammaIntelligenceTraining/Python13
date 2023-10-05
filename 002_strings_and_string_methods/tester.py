string_sample1 = 'Hello world world'
                 #0123456789
                        #-5-4-3-2-1
string_sample2 = 'first leTter is loWercase. new-sentnce'
string_sample3 = '*   *f*extra symbols   '
german_sample = 'der fluß'

print(len(string_sample1))
print(type(len(string_sample1)))

# [START:END:STEP]
# print(string_sample1[len(string_sample1) - 1])
# print(string_sample1[0])
# print(string_sample1[-17])
# print('Hello ' + string_sample1[6:11])
# x = string_sample1[6:11]
# print(x[0:2])
# print(string_sample1[6:11][0:2][1])
# print(string_sample1)
# print(string_sample1[5:])
# print(string_sample1[0:14:3])
# print(string_sample1[-6:])
# print(string_sample1[::-1])
# print('hello world'[::-1])
# print(string_sample1[0:5] + string_sample2[5:12])

# print('world' in string_sample1)
# print('a' > 'A')
# print('World' == 'world')
#
# print(string_sample2.upper())
# print('HELLO WORLD'.isupper())
#
# print(german_sample.lower())
# print(german_sample.casefold())
#
# print('HELLO world'.swapcase())
#
# print(string_sample2.capitalize())
#
# print(string_sample2.title())
# print('Hello World'.istitle())

# print(string_sample3.strip('* fesl'))
# print(string_sample1.replace('world', '',1))
#
# print('Hello people, of planet Earth'.split(', '))
#
# a, b, c = input('Enter a, b, c: ').split()
# print(a, b, c)

# print(string_sample1.count('world', 0, 12))
# print(string_sample1.find('world', 7))

# print('Hello', 'Planet', 123, sep='', end='\n')
# print(len('Wo\n\nrld'))
# print('World')
# print('That\'s it')
# print("My favourite book is \"Harry Potter\"")
# print('\tC:\Hello\\new')
# print(r'\tHello\ne\'w')

# name = 'John'
# salary = 1000
# age = 20
# salary_str = '{2}s salary is {1}. Age: {0}{0}{0}{2}'
# print(salary_str.format(name, salary, age))

# salary_str = '{user_name}s salary is {user_salary:.2f}. Age: {user_age}'
# print(salary_str.format(user_name=name, user_age=age, user_salary=salary))

# Formated string used in Python 2
# x = 12231.3456789
# y = 131.1314
# print('The value of x is %.4f' % x)
# print('The value of y is %.2f' % y)
#
# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500
#
# emp_string = 'Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' % {'name': emp_name, 'salary': emp_salary, 'age': emp_age}
# print(emp_string)
name = 'John'
salary = 1000.232
age = 20

print(f'{name.upper()}s salary is {int(salary)}. He is {age} years old.')

byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_sting.decode('utf-16'))

text = 'Hello world!'
print(text.encode('utf-16'))