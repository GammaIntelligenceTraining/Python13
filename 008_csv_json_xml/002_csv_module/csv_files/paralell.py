import csv
with open('2019.csv', 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    print(headers)




while True:
    user_choise = input("Please choose:\n"
                        "1.Top 10 over all rank\n"
                        "2.Top 10 worst countries by rank\n"
                        "3.Top 10 GDP countries\n"
                        "4.Top 10 Social support\n"
                        "5.Top 10 Healthy life expectancy\n"
                        "6.Top 10 by Freedom to make life choices\n"
                        "7.Top 10 by Generosity\n"
                        "8.Top 10 by Perceptions of corruption\n"
                        "10.Authors opinion about worst country ever.\n"
                        "--> ")
    if user_choise.lower() == "exit":
        break
    try:
        int(user_choise)
        if len(user_choise) > 2:
            raise UserWarning
    except ValueError:
            print("Убери грабли с клавиатуры!")
    except UserWarning:
        if len(user_choise) > 2:
            print("Глазза раззуй и посмотри, сколько у тебя возможностей выбрать!!!")
        else:
            print("kro")