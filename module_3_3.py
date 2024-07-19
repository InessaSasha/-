# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(10)
print_params(10, False)
print_params(10, False, 'Жизнь')

# Проверьте, работают ли вызовы
print_params(b=25)
print_params(c=[1, 2, 3])


# 2.Распаковка параметров:

values_list =[1, 'привет', False]
values_dict = {'a': True, 'b': 56, 'c': 'Пока'}

print_params(*values_list)
print_params(**values_dict)

print_params(*values_list, **values_dict) #убрать, чтобы сработал код ниже
#здесь не будет работать, потому что количество значений внутри списка и словаря больше, чем
#количество элементов в функции, но будет работать, если фунцию записать так
#def print_params(*args, **kwargs):
    #print(args,kwargs)

# 3.Распаковка + отдельные параметры:
values_list_2 = ['привет', False]
print_params(*values_list_2, 42)
