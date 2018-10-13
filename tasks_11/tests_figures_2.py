from figures_2 import (NonExistentFigureError, Triangle, Rectangle, Square, Trapeze, Circle)

# Triangle


def test_triangle_ok():
    triangle = Triangle(10, 10, 10)

    if triangle.area() == 43.301270189221924 and \
       triangle.perimeter() == 30 and \
       triangle.height() == 8.660254037844386:
        print('Ok')
    else:
        print('Not Ok')


def test_triangle_not_implemented_error():
    triangle = Triangle(10, 10, 10)

    try:
        if triangle.volume():
            print('Not Ok')
    except NotImplementedError:
        print('Ok')


def test_triangle_non_existent_figure_error():
    try:
        triangle = Triangle(0, 0, 0)
        print('Not Ok')
    except NonExistentFigureError:
        print('Ok')


# Rectangle


def test_rectangle_ok():
    rectangle = Rectangle(10, 20)

    if rectangle.area() == 200.00 and \
       rectangle.perimeter() == 60.00:
        print('Ok')
    else:
        print('Not Ok')


def test_rectangle_not_implemented_error():
    rectangle = Rectangle(10, 20)

    try:
        if rectangle.volume():
            print('Not Ok')
    except NotImplementedError:
        print('Ok')


def test_rectangle_non_existent_figure_error():
    try:
        rectangle = Rectangle(0, 0)
        print('Not Ok')
    except NonExistentFigureError:
        print('Ok')

# Square


def test_square_ok():
    square = Square(10)

    if square.area() == 100.00 and \
       square.perimeter() == 40.00:
        print('Ok')
    else:
        print('Not Ok')


def test_square_not_implemented_error():
    square = Square(10)

    try:
        if square.volume():
            print('Not Ok')
    except NotImplementedError:
        print('Ok')


def test_square_non_existent_figure_error():
    try:
        square = Square(0)
        print('Not Ok')
    except NonExistentFigureError:
        print('Ok')


# Trapeze


def test_trapeze_ok():
    trapeze = Trapeze(6, 10, 5, 7)

    if trapeze.area() == 39.191835884530846 and \
       trapeze.perimeter() == 28.00 and \
       trapeze.height() == 4.898979485566356:
        print('Ok')
    else:
        print('Not Ok')


def test_trapeze_not_implemented_error():
    trapeze = Trapeze(6, 10, 5, 7)

    try:
        if trapeze.volume():
            print('Not Ok')
    except NotImplementedError:
        print('Ok')


def test_trapeze_non_existent_figure_error():
    try:
        trapeze = Trapeze(0, 0, 0, 0)
        print('Not Ok')
    except NonExistentFigureError:
        print('Ok')


# Circle


def test_circle_ok():
    circle = Circle(10)

    if circle.area() == 314.1592653589793 and \
       circle.perimeter() == 62.83185307179586:
        print('Ok')
    else:
        print('Not Ok')


def test_circle_not_implemented_error():
    circle = Circle(10)

    try:
        if circle.volume():
            print('Not Ok')
    except NotImplementedError:
        print('Ok')


def test_circle_non_existent_figure_error():
    try:
        circle = Circle(0)
        print('Not Ok')
    except NonExistentFigureError:
        print('Ok')


test_triangle_ok()
test_triangle_not_implemented_error()
test_triangle_non_existent_figure_error()
print()
test_rectangle_ok()
test_rectangle_not_implemented_error()
test_rectangle_non_existent_figure_error()
print()
test_square_ok()
test_square_not_implemented_error()
test_square_non_existent_figure_error()
print()
test_trapeze_ok()
test_trapeze_not_implemented_error()
test_trapeze_non_existent_figure_error()
print()
test_circle_ok()
test_circle_not_implemented_error()
test_circle_non_existent_figure_error()
