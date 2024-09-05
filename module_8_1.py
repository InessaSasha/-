def add_everything_up(a, b):
    try:
        if type(a) == type(b):
            # проверяем числа или нет
            if isinstance(a, (int, float)):
                return a + b
            # проверяем строки или нет
            elif isinstance(a, str):
                return a + b
        else:
            return str(a) + str(b)
    except TypeError:
        # возвращаем если у нас a и b разных типов
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))