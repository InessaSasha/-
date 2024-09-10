import os
#Используйте os.walk

directory = '/Users/gospoza/PycharmProjects/homework5/Git/домашка'

for root, dirs, files in os.walk(directory):
    print(f"Каталог: {root}")
    for dir in dirs:
        print(f"  Подкаталог: {dir}")
    for file in files:
        print(f"  Файл: {file}")

#Примените os.path.jo

file_path = os.path.join('my_folder', 'subfolder', 'file.txt')
print(file_path)

#Используйте os.path.getmtime и модуль time
import time

file_path = '/Users/gospoza/PycharmProjects/homework5/Git/домашка/test.txt'

file_time = os.path.getmtime(file_path)
read_time = time.ctime(file_time)
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
print(f"Время последнего изменения: {read_time}")

#Используйте os.path.getsize

file_size = os.path.getsize(file_path)
print(f"Размер файла : {file_size}")

#Используйте os.path.dirname

parent_dir = os.path.dirname(file_path)
print(f'Обнаружен файл: {file}, Путь: {file_path}, '
      f'Размер: {file_size} байт, Время изменения: '
      f'{formatted_time}, Родительская директория: {parent_dir}')
