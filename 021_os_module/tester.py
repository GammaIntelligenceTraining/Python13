import os

# os.chdir('../020_email_sender/')
# print(os.getcwd())
# print(os.listdir())

# os.mkdir('test/test2')
# os.makedirs('test/test2/test3')

# os.removedirs('test/test2')

# os.rename('sample.mp3', 'sample.png')

# print(os.stat('sample.png'))
# information = os.walk('../')
# print(information)
#
# for dirpath, dirnames, filenames in information:
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()
filename = 'sample.txt'
# print(os.environ.get('HOMEPATH') + '\\' + filename)

# file_path = os.path.join('user', filename)
# print(file_path)

print(os.path.basename('/somedir/sample.txt'))
print(os.path.dirname('/somedir/another/onemore/sample.txt'))
print(os.path.split('/somedir/another/onemore/sample.txt'))
print(os.path.splitext('/somedir/another/onemore/sample.txt'))

print(os.path.exists('text'))
print(os.path.isdir('/somedir'))
print(os.path.isfile('sample.txt'))
