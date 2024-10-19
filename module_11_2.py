from pprint import pprint
def introspection_info(obj):
    info = {
        'Тип объекта': type(obj),
        'Атрибуты объекта': dir(obj),
        'Методы объекта': [method for method in dir(obj) if callable(getattr(obj, method))],
        'Модуль': getattr(obj, '__module__', '__main__'),
    }
    return info
number_info = introspection_info(42)
pprint(number_info)

