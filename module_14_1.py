import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#1. Заполняем 10 записями

#for i in range(1, 11):
    #cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   #(f"newuser{i}", f"example{i}@gmail.com", 10 + (i - 1) * 10, "1000"))

#2. Обновляем balance у каждой 2ой записи начиная с 1ой на 500

#cursor.execute("""UPDATE Users SET balance = 500
#WHERE id IN (SELECT id FROM(SELECT id, ROW_NUMBER()
#OVER (ORDER BY id) AS rn FROM Users) AS numbered WHERE rn % 2 = 1)""")


#3. Удаляем каждую 3ую запись в таблице начиная с 1ой:

#cursor.execute("""DELETE FROM Users
#WHERE id IN (SELECT id FROM(SELECT id, ROW_NUMBER()
#OVER (ORDER BY id) AS rn FROM Users) AS numbered WHERE rn % 3 = 1)""")

#4. Сделаем выборку всех записей при помощи fetchall(), где возраст не равен 60

cursor.execute("SELECT * FROM Users WHERE age !=?", (60,))
users = cursor.fetchall()

for user in users:
    print(user)


connection.commit()
connection.close()