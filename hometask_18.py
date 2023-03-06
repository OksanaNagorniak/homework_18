# Создайте супер класс Shape и его наследников Triangle, Rectangle.
# Класс Shape содержит абстрактный метод draw
# Класс Triangle в инициализаторе принимает параметр width:
# int - ширина треугольника и реализует метод draw (Выводит в консоль треугольник с шириной width)
# Класс Rectangle в инициализаторе принимает параметр
# width: int и height: int - ширина, высота прямоугольника и реализует метод draw
# (Выводит в консоль прямоугольник с шириной width и высотой height)
# Создайте список с этими фигурами и в
# цикле вызовите метод draw у этих обьектов
#
#
# P.S. Треугольник может быть любой (Равносторонний, Равнобедренный, Разносторонним)
# главное чтобы состоял и был заполнен символом '*'.
#
# Прямоугольник тоже должен состоять и быть заполнен символом '*'.
#
# Важно: Используйте аннотации!


import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def draw(self) -> object:
        pass


class Triangle(Shape):
    def __init__(self, width: int) -> object:
        # super().__init__(self)
        self.width = width
        # self.char ='*'

    def draw(self) -> object:
        for i in range(0, self.width):
            for j in range(0, self.width - i - 1):
                print(end=" ")
            for j in range(0, i + 1):
                print("*", end=" ")
            print()


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def draw(self) -> object:
        for i in range(self.width):  # print("*" * self.width)
            for j in range(self.height):
                print("*", end=" ")
            print()


list_1 = [Triangle(5), Rectangle(4, 5), Rectangle(2, 3), Triangle(4)]
for obj in list_1:
    obj.draw()
    print('\n')
