"""
Задача 2
Реализовать программу подсчета площади, периметра, объема геометрических фигур
(треугольник, прямоугольник, квадрат, трапеция, окружность).
Если одна из фигур не поддерживает вычисление одного из свойств, в программе
должно быть вызвано исключение с человеко-читабельным сообщением
и корректно обработано.
"""

import math


class NonExistentFigureError(Exception):
    def __str__(self):
        return 'Такой фигуры не существует.'


class Figure:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def volume(self):
        raise NotImplementedError


# Класс, описывающий треугольник
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise NonExistentFigureError

        if self.side_a + self.side_b < side_c or \
           self.side_a + self.side_c < side_b or \
           self.side_b + self.side_c < self.side_a:
            raise NonExistentFigureError

    def height(self):
        half_sum = 1/2 * (self.side_a + self.side_b + self.side_c)
        height = 2 * math.sqrt(half_sum * (half_sum - self.side_a) *
                               (half_sum - self.side_b) *
                               (half_sum - self.side_c)) / self.side_a
        return height

    def area(self):
        area = 1/2 * self.side_a * self.height()
        return area

    def perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter

    def __str__(self):
        return 'Ваша фигура: Треугольник\nПлощадь = {:.2f}\nПериметр = {:.2f}\nВысота = {:.2f}'\
            .format(self.area(), self.perimeter(), self.height())

    @classmethod
    def create_from_input(cls):
        try:
            side_a = float(input('Введите размер первой стороны: '))
            side_b = float(input('Введите размер второй стороны: '))
            side_c = float(input('Введите размер третьей стороны: '))
        except ValueError:
            print('\nВведено некорректное значение.')
            return

        triangle = Triangle(side_a, side_b, side_c)
        return triangle


# Класс, описывающий прямоугольник
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

        if self.length <= 0 or self.width <= 0 or self.length == self.width:
            raise NonExistentFigureError

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def __str__(self):
        return 'Ваша фигура: Прямоугольник\nПлощадь = {:.2f}\nПериметр = {:.2f}'\
            .format(self.area(), self.perimeter())

    @classmethod
    def create_from_input(cls):
        try:
            length = float(input('Введите длину прямоугольника: '))
            width = float(input('Введите ширину прямоугольника: '))
        except ValueError:
            print('\nВведено некорректное значение.')
            return

        rectangle = Rectangle(length, width)
        return rectangle


# Класс, описывающий квадрат
class Square(Figure):
    def __init__(self, side):
        self.side = side

        if self.side <= 0:
            raise NonExistentFigureError

    def area(self):
        area = self.side ** 2
        return area

    def perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def __str__(self):
        return 'Ваша фигура: Квадрат\nПлощадь = {:.2f}\nПериметр = {:.2f}'\
            .format(self.area(), self.perimeter())

    @classmethod
    def create_from_input(cls):
        try:
            side = float(input('Введите размер стороны квадрата: '))
        except ValueError:
            print('\nВведено некорректное значение.')
            return

        square = Square(side)
        return square


# Класс, описывающий трапецию
class Trapeze(Figure):
    def __init__(self, base_a, base_b, side_c, side_d):
        self.base_a = base_a
        self.base_b = base_b
        self.side_c = side_c
        self.side_d = side_d

        if self.base_a <= 0 or self.base_b <= 0 or self.side_c <= 0 or self.side_d <= 0 or base_a >= base_b:
            raise NonExistentFigureError
        # если невозможно расчитать площадь, значит такой трапеции не может существовать
        # будет вызван NonExistentFigureError
        self.area()

    def height(self):
        height = 2 * self.area() / (self.base_a + self.base_b)
        return height

    def area(self):
        try:
            x = (self.base_b - self.base_a) ** 2 + self.side_c ** 2 - self.side_d ** 2
            y = 2 * (self.base_b - self.base_a)
            temp = self.side_c ** 2 - (x / y) ** 2

            area = (self.base_a + self.base_b) / 2 * math.sqrt(temp)
        except ValueError:
            raise NonExistentFigureError

        return area

    def perimeter(self):
        perimeter = self.base_a + self.base_b + self.side_c + self.side_d
        return perimeter

    def __str__(self):
        return 'Ваша фигура: Трапеция\nПлощадь = {:.2f}\nПериметр = {:.2f}\nВысота = {:.2f}'\
            .format(self.area(), self.perimeter(), self.height())

    @classmethod
    def create_from_input(cls):
        try:
            base_a = float(input('Введите размер первого основания: '))
            base_b = float(input('Введите размер второго основания: '))
            side_c = float(input('Введите размер первой стороны: '))
            side_d = float(input('Введите размер второй стороны: '))
        except ValueError:
            print('\nВведено некорректное значение.')
            return

        # try:
        trapeze = Trapeze(base_a, base_b, side_c, side_d)
        return trapeze
        # except NonExistentFigureError:
        #     print('Такой фигуры не существует.')


# Класс, описывающий окружность
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

        if self.radius <= 0:
            raise NonExistentFigureError

    def area(self):
        area = math.pi * self.radius ** 2
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def __str__(self):
        return 'Ваша фигура: Круг\nПлощадь = {:.2f}\nДлина окружности = {:.2f}'\
            .format(self.area(), self.perimeter())

    @classmethod
    def create_from_input(cls):
        try:
            radius = float(input('Введите радиус окружности: '))
        except ValueError:
            print('\nВведено некорректное значение.')
            return

        circle = Circle(radius)
        return circle


create_figure = {
    '1': Triangle.create_from_input,
    '2': Rectangle.create_from_input,
    '3': Square.create_from_input,
    '4': Trapeze.create_from_input,
    '5': Circle.create_from_input,
}


def main():
    while True:
        figure = input("""
    1 - Треугольник
    2 - Прямоугольник
    3 - Квадрат
    4 - Трапеция
    5 - Окружность
    
    Выберите номер фигуры: """)

        if figure == '':
            break

        if figure not in create_figure:
            print('\nВведён неверный номер фигуры.')
            continue

        try:
            figure_object = create_figure[figure]()
        except NonExistentFigureError:
            print('\nТакой фигуры не существует.')
            continue

        if figure_object is None:
            continue

        while True:
            method = input("""
        1 - Площадь
        2 - Периметр
        3 - Объём
        
        
        Выберите параметр для расчёта: """)

            if method == '':
                break

            input_list = {
                '1': [figure_object.area, '\nВаша фигура: {}\nПлощадь = {:.2f}'],
                '2': [figure_object.perimeter, '\nВаша фигура: {}\nПериметр = {:.2f}'],
                '3': [figure_object.volume, '\nВаша фигура: {}\nОбъём = {:.2f}'],
            }

            try:
                if method in input_list:
                    print(input_list[method][1].format(
                        type(figure_object).__name__,
                        input_list[method][0]()
                    ))
                else:
                    print('\nВведён неверный параметр для расчёта.')
            except NotImplementedError:
                print('\nТакого параметра у данной фигуры не существует.')


if __name__ == '__main__':
    main()
