# Gamma Intelligence Training 2
# 10008218

# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
print(example_string1[:2] + example_string1[-2:])
# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())

# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
print(example_string3.strip('*'))


# Write a code to return "Hello my name is Jack"
example_string4 = "hello my naMe is jack"
print(example_string4.capitalize().replace('jack', 'Jack'))
# print(example_string4[:-4] + example_string4[-4:].capitalize())


# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(f'{var2.capitalize()}, {var3.lower()} {var1.capitalize()}')



# Write a code to return byte_string text value
# 'utf-8' 'utf-16'
byte_string = b"\316\273"
print(byte_string.decode('utf8'))
print(byte_string.decode('utf16'))
print(byte_string.decode('cp1257'))

