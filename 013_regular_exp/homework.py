import re

text = 'asdasdasdasdasas32 1312SADASDASdsads'
hex_color = re.compile(r'#\b[0-9a-fA-F]{6}\b')
plus_numbers = re.compile(r'(\d)[^+]')
time_pattern = re.compile(r'\b([01]\d|2[0-3]):([0-5]\d)\b')
name_pattern = re.compile(r'([A-Za-z-]+ [A-Za-z-]+)\n')
address_pattern = re.compile(r'\d{3} [A-Za-z0-9-]+ St\., [A-Za-z- \']+ [A-Z]{2} \d{5}')
illegal_symbols = re.compile(r'[^A-Za-z0-9]')
idcode = re.compile(r'[1-8]\d\d(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')

# with open('people.txt', 'r') as file:
#     data = file.read()


# people_matches = re.findall(name_pattern, data)
# people_matches = list(people_matches)
# print(len(people_matches))
# for person in people_matches:
#     print(person)
# address_matches = re.findall(address_pattern, data)
# print(len(address_matches))

matches = re.findall(illegal_symbols, text)
if matches:
    print('NOK')
else:
    print('OK')
# if len(matches) == len(text):
#     print("OK")
# else:
#     print("NOK")
# print(matches)
# for match in matches:
#     print(match)