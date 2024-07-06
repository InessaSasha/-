my_dict = {'Sasha': 1993, 'Elena': 1991, 'Kate': 2000}
print(my_dict)
print(my_dict['Sasha'])
print(my_dict.get('Alex', 'Такого значения в словаре нет'))
my_dict.update({'Liza': 1980,
                'Oleg': 2005})
print(my_dict)
z = my_dict.pop('Sasha')
print(z)
print(my_dict)
#задание на множества
my_set = {45, 'Leto', True, True, 3, 5, 5, 45}
print(my_set)
my_set.add(67)
my_set.add('Son')
print(my_set)
#либо вариант через update
my_set.update([356, 98])
print(my_set)
my_set.discard(356)
print(my_set)
