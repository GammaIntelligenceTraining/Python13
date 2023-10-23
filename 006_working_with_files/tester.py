# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

# file = open('lor.txt', 'r', encoding='UTF8')
#
# print(file.name)
# print(file.mode)
# print(file.encoding)
# file.close()
# print(file.closed)

# with open('lor.txt', 'r', encoding='UTF8') as file:
#     # file_content = file.read()
#     # file_content = file.readlines()
#     # file_content = file.readline()
#     file_content = file.read(20)
#     print(file_content)
#     file_content = file.read()
#     print(file_content)
#
#
# print(file_content)
# print(type(file_content))
# print(len(file_content))

# with open('lor.txt', 'r', encoding='UTF8') as file:
#     read_size = 100
#     file_content = file.read(read_size)
#     print(file_content)
#     file.seek(500)
#     file_content = file.read(read_size)
#     print(file_content)

# with open('lor_copy.txt', 'x', encoding='UTF8') as file:
#     file.write('Hi there\n')
#     file.write('Hello world\n')
#     file.write(input('Enter name: '))


# with open('lor_copy.txt', 'r+', encoding='UTF8') as file:
#     data = file.read().upper()
#     file.seek(0)
#     file.write(data)

with open('text_files/python_picture.jpg', 'rb') as picture:
    data = picture.read()


with open('text_files/python_picture_copy.png', 'wb') as picture_copy:
    picture_copy.write(data)

print(data)
