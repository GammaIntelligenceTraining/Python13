# empty = []
# empty = list()
# print(type(empty))
# print(bool(empty))

# world = 'world'
#
# filled_list = [12312, 123.1231, 'Hello', world, [1, [4, 5, 'Hello'], 3]]
# print(len(filled_list))
# print(filled_list[1::2])
# courses = ['History', 'Programming', 'Math', 'Literature', 'Physics', '123', 'art']
# numbers = [1, 5, 6, 8, 3, -4, 2, 0.23]

# test = [1, 2, 3]
# test[1] = 'Hello'
# print(test)

# courses.append('English')
# courses.insert(1, 'Art')
# extra_courses = ['English', 'Art']
# courses.extend(extra_courses)
# courses.remove('Math')
#
# removed = courses.pop(1)
# print(removed)
# courses.reverse()
# courses.sort(reverse=True)
# print(courses)
#
# numbers.sort()
# print(numbers)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# print(courses[:3] + numbers + courses[3:])
# print(courses)
# print(courses.index('Math', 3))
# print([1, 2, 3] in courses)

# courses_str = ', '.join(courses)
# print(courses_str)
# print('hello world'.split('l'))

# a = ['One', 'Two', 'Three']
# b = a.copy()
# a[1] = 'Four'
# b[2] = 'Five'
# print(a, b)
# courses = ('History', 'Programming', 'Math', 'Literature', 'Physics', '123', 'art')
# numbers = (1, 5, 6, 8, 3, -4, 2, 0.23)

# empty = ()
# empty = tuple()
# empty = (1,)
# print(type(empty))

# print(courses[:4] + numbers[2:5])

courses = {'History', 'Programming', 'Math', 'Literature', 'Physics', '123', 'Math'}
numbers = {1, 5, 6, 8, 3, -4, 2, 4.23, -12.12}

# empty = set()
# print(type(empty))
# print(courses)
# courses.remove('Math')
# print(numbers)

# set1 = {'Math', 'History', 'Programming', 'Physics'}
# set2 = {'Art', 'Physics', 'Design', 'History'}
# set3 = {'Art', 'Design'}
#
# print(set2.intersection(set1))
#
# print(set1.difference(set2))
# print(set2.difference(set1))
#
# print(set3.issubset(set2))
# print(set2.issuperset(set3))
#
# x = [1, 2, 3]
# x[1:] = [9]
# print(x)
#
# x = [1, 2, 3, 1, 2, 3, 1, 2, 3]
# x = list(set(x))
# print(x)

for number in range(10):
    if number % 2 == 0:
        print(number ** 2)
