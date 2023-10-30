import csv

with open('csv_files/2019.csv', 'r') as file:

    data = csv.reader(file)
    headers = next(data)
    data = list(data)

top = 10
column = 3

# indexes = list(enumerate(headers))

def sort_by_column(column, top):
    data_copy = data.copy()
    data_copy.sort(key=lambda x: x[column])

    result = []
    while len(result) < top:
        result.append(data_copy.pop())

    return result

def change_top():
    global top
    user_top = int(input('Enter top ammount: '))
    top = user_top

def print_result(result):
    # Print all countries in result list
    pass

while True:
    user_choice = input('1.GDP per capita\n'
                        '2.Social support\n'
                        '3.Healthy life expectancy\n'
                        '4.Freedom to make life choices\n'
                        '5.Generosity\n'
                        '6.Perceptions of corruption\n'
                        '7.Change TOP amount\n'
                        '0.Exit\n'
                        '--> ')
    if user_choice == '1':
        print(sort_by_column(3, top))
    elif user_choice == '2':
        print(sort_by_column(4, top))
    elif user_choice == '3':
        print(sort_by_column(5, top))
    elif user_choice == '4':
        print(sort_by_column(6, top))
    elif user_choice == '5':
        print(sort_by_column(7, top))
    elif user_choice == '6':
        print(sort_by_column(8, top))
    elif user_choice == '7':
        change_top()
    elif user_choice == '0':
        print('Good bye!')
        break
    else:
        print('Choice out of range!')

