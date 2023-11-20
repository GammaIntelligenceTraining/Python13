import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='sakila'
)
# db.autocommit = True

mycursor = db.cursor()
#
# mycursor.execute('INSERT INTO car (make, model, year) VALUES ("VW", "PASSAT", "2000");')
# mycursor.execute('INSERT INTO car (make, model, year) VALUES ("Honda", "Civic", "2005");')
# mycursor.execute('INSERT INTO car (make, model, year) VALUES ("Toyota", "Corolla", "2023");')

# sql_formula = "INSERT INTO car (make, model, year) VALUES (%s, %s, %s);"
# mycar = ("Honda", "CR-V", 2000)
# # mycursor.execute(sql_formula, mycar)
#
# cars = [("VAZ", "2103", 1985), ("Seat", "Leon", 2020), ("Ferrari", "360", "1990")]
# mycursor.executemany(sql_formula, cars)
#
# for car in cars:
#     mycursor.execute(f'INSERT INTO car (make, model, year) VALUES (\'{car[0]}\', \'{car[1]}\', \'{car[2]}\');')

# db.commit()
# for line in mycursor:
#     print(line)


# mycursor.execute("SELECT * FROM actor;")

# actor = mycursor.fetchall()
# print(actor)
# for _id, name, surname, date_added in actor:
#     print(f'{name.title()} {surname.title()}')

# actor1 = mycursor.fetchone()
# actor2 = mycursor.fetchone()
# print(actor1)
# print(actor2)

# for x in range(300):
#     print(mycursor.fetchone())

sql_formula = "SELECT * FROM actor WHERE first_name = %s"
mycursor.execute(sql_formula, ("PENELOPE",))
print(mycursor.fetchall())