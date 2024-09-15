class StepValueError(ValueError):
    pass
class Iterator:

    def __init__(self, start, stop, step=1):
        #здесь мы сразу ловим ошибку, если шаг у нас вдруг 0
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        #фиксируем изначально позицию итерации со стартом
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0:
            # проверяем pointer больше stop, либо меньше stop.
            if self.pointer >= self.stop:
                raise StopIteration
        else:
            if self.pointer <= self.stop:
                raise StopIteration
            #текущее значение положения итерации
        current_value = self.pointer
        self.pointer += self.step
        return current_value
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()