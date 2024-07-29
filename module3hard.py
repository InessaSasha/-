def sum_elements(data_structure):
  #суммируем все длины строк, ключей, значений, чисел
  total = 0 # сюда запишем общую сумму
  
  for element in data_structure:
    if isinstance(element, int):
      total += element
    elif isinstance(element, str):
      total += len(element)
    elif isinstance(element, (list, tuple, set)):
      total += sum_elements(element)
    elif isinstance(element, dict):
      for key, value in element.items():
        total += len(key)  # Суммируем длину ключа
        total += sum_elements([value])  # суммируем значения любых элементов, которые могут быть внутри
    else:
      pass
  return total

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = sum_elements(data_structure)
print(f"Сумма элементов: {result}")
