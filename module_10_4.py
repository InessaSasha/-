from threading import Thread
from queue import Queue
import random
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)
        print(f"{self.name} покушал(-а) и ушел(-ла)")

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)
        self.left_guests = []

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = self.find_free_table()
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest and table.guest.is_alive() for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    if table.guest.name not in self.left_guests:
                        print(f"{table.guest.name} покушал(-а) и ушел(-ла)")
                        print(f"Стол номер {table.number} свободен")
                        self.left_guests.append(table.guest.name)
                    table.guest = None

                    if not self.queue.empty():
                        new_guest = self.queue.get()
                        # Проверка на повторный вывод здесь!
                        if new_guest.name not in self.left_guests:
                            table.guest = new_guest
                            new_guest.start()
                            print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()