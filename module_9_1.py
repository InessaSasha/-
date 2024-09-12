def apply_all_func(int_list, *functions):
    results = {}
    #перебираем все функции
    for funcs in functions:
        #записываем в значение имя функции, а в ключ результат функции
        results[funcs.__name__] = funcs(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))