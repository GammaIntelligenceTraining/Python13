# def no_parameter():
#     # print('Hello world!')
#     return 'Hello world!'
#
# # print(no_parameter())
#
# x = no_parameter().upper()
# print(x)

# def with_params(number1, number2):
#     # print(number1 ** number2)
#     return number1 ** number2
# # with_params(10)
# # with_params(20)
# # with_params(30)
# # b = 40
# # with_params(b)
# # x = [50, 60, 70]
# # with_params(x[0])
#
# print(with_params(12, 3))

# def odd_or_even(number):
#     # if number % 2 == 0:
#     #     return 'Even'
#     # else:
#     #     return 'Odd'
#     if number == 7:
#         return number ** 2
#     return number ** 3
# #
# # print(odd_or_even(7))
# #
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# #
# for num in x:
#     print(f'{num} is {odd_or_even(num)} number')
#
# print(range(10))

# def say_hello(first_name, last_name, age, gender):
#     if gender == 'male':
#         return f'This is {first_name} {last_name}. He is {age} years old.'
#     elif gender == 'female':
#         return f'This is {first_name} {last_name}. She is {age} years old.'
#
# first = input('Enter name: ')
# last = input('Enter lastname: ')
# print(say_hello(first, last, 20, 'female'))

# def sum_three_or_two(num2, *args, **kwargs):
#     for arg in args:
#         print(arg)
#     print(kwargs)
#     # return num1 + num2 + num3
#
# x = sum_three_or_two(3, 4, 0, 1, 2, 4, 'asd', 'weq', name='Jack', surname='Smith')
# print(x)

# x = [1, 2, 3]
# y = [*x, 5, *x, 7]
# # y.sort()
# print(y)


# def tester(num1, num2, num3):
#     print(num1, num2, num3)
#
# tester(1, 2, 3)
# tester(num3=1, num2=2, num1=3)

# a = 1
# b = 2
#
# def tester():
#     global a, b, c
#     a += 10
#     b = 20
#     c = 10
#     print(a, b, c)
#
# tester()
# tester()
# tester()

# tester()
# print(a, b, c)
# a += 10
# tester()

# import helpers
# print(helpers.sqrt(144))
# print(helpers.format_name('roman', 'KUTSELEPA'))

# def hello():
#     print('Hello')
#
#
# def wrapper(func):
#     print('Starting')
#     func()
#     print('Ending')
#
# wrapper(hello)

order = [
    {'size': 'small', 'qty': 35, 'width': 60, 'height': 40},
    {'size': 'medium', 'qty': 20, 'width': 80, 'height': 60},
    {'size': 'large', 'qty': 15, 'width': 90, 'height': 90},
]

# area = width * height
# perimeter = (width + height) * 2

# TOTAL CARPET MATERIAL XXXX m2
# TOTAL EDGE MATERIAL XXXX m