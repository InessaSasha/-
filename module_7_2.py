
def custom_write(file_name, strings):
    position_strings = {}
    file = open(file_name, 'w', encoding='utf-8')

    #взяла функцию в инете. изначально пробовала без старт, но тогда нумерация строк с 0,
    #ввела start=1, чтобы нумерация строк была с 1

    for i, string in enumerate(strings, start=1):
        position = file.tell() # смотрим текущую позицию курсора
        file.write(string + '\n') # записываем строку
        position_strings[(i, position)] = string #здесь идет добавление в словарь
    file.close()
    return position_strings

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
