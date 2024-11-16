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

#cursor.execute("SELECT * FROM Users WHERE age !=?", (60,))
#users = cursor.fetchall()

##    print(user)


cursor.execute("DELETE FROM Users WHERE id=?", ('6',))

cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]
print(total1)

cursor.execute("SELECT SUM(balance) FROM Users")
total2 = cursor.fetchone()[0]
print(total2)

cursor.execute("SELECT AVG(balance) FROM Users")
total3 = cursor.fetchone()[0]
print(total2/total1)

connection.commit()
connection.close()