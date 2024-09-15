# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

list_1 = list(map(lambda x, y: x == y, first, second))
print(list(list_1))

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        #открываем наш файл в режиме "а"
        with open(file_name, 'a') as file:
            #проходим по всем элементам data_set
            for data in data_set:
                #преобразуем данные в строку
                file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:

from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        # выбираем случайное слово из списка words
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())







