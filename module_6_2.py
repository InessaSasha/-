class Vehicle:
    __COLOR_VARIANTS = ['orange', 'yellow', 'grey', 'black', 'white']
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def set_color(self, new_color: str):
        new_color_lower = new_color.lower()
        #нашла эту конструкцию, чтобы понизить регистр в списке во всём
        if new_color_lower in [color.lower() for color in Vehicle.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    def print_info(self):
        print(f"Модель: {self.get_model()}")
        print(f"Мощность двигателя: {self.get_horsepower()}")
        print(f"Цвет: {self.get_color()}")
        print(f"Владелец: {self.owner}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)


# Текущие цвета __COLOR_VARIANTS = ['orange', 'yellow', 'grey', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
#здесь я исправила вводные данные, т.к engine_power  должно быть числом
#при тех данных, что были даны в задании, всплывает ошибка

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('pink')
vehicle1.set_color('YELLOW')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
