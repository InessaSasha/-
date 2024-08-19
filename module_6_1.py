class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False #Животное изначально не накормлено
        self.name = name

    def eat(self, food):
        if food.edible: #проверяем съедобно ли растение
            print(f"{self.name} съел {food.name}")
            self.fed = True #меняем False на True т.к животное накормлено
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False #животное не стало есть и погибло

class Plant:
    edible = False # растение изначально несъедобное
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True  # фрукт изначально съедобное
    def __init__(self, name):
        super().__init__(name) # super() берем, чтобы взять атрибуты из
        # родительского класса Plant

# Создаем объекты
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

