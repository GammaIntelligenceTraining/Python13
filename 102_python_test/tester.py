# first_name, last_name, age = input('Enter name, surname and age. Use "," as separator: ').split(', ')
# # test = input().split(', ')
# print(f'Hello, {last_name} {first_name}. Your age is: {age}')
#
# # a, b, c = [1, 2, 3]
# # print(a, b, c)

# import math
# a = 3
# b = 4
# c = (a ** 2 + b ** 2) ** 0.5
# c = math.sqrt(a ** 2 + b ** 2)
# print(c)

# a, b, c = input('Enter sides A, B and C: ').split()
# if float(c) ** 2 == float(a) ** 2 + float(b) ** 2:
#     print(True, 'This is right triangle.')
# else:
#     print(False, 'This is not right triangle.')

# user_list = input('Enter list elements: ').split(', ')
# user_list.reverse()
# for item in user_list:
#     print(item)
#
# print(user_list[::-1])

# a = (1, 2, 3, 5, 8)
#
# b = (8,2,5)
# print(id(a))
# # a = a[:2] + b + a[2:]
# a = list(a)
# print(id(a))
# for num in b[::-1]:
#     a.insert(2, num)
# a = tuple(a)
# print(id(a))
# print

# test_list = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10, 10, 4]
#
# result = {}
#
# for num in test_list:
#     result[num] = test_list.count(num)
#
# res = []
# for key in result.keys():
#     if result[key] == max(result.values()):
#         res.append(key)
#
#
# print(res)

# max_count = 0
# result = []
#
# for num in test_list:
#     if test_list.count(num) > max_count:
#         max_count = test_list.count(num)
#
# for num in test_list:
#     if test_list.count(num) == max_count and num not in result:
#         result.append(num)
#
# print(result)
#
# seconds = 1234565
#
# days = seconds // (24 * 60 * 60)
# seconds %= 24 * 60 * 60
# hours = seconds // (60 * 60)
# seconds %= 60 * 60
# minutes = seconds // 60
# seconds %= 60
# print(f'{days}:{hours}:{minutes}:{seconds}')
