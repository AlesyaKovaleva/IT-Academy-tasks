"""
Задача 0
Реализовать модуль, содержащий следующие функции декораторы:
- декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
- декоратор, позволяющий записывать время работы функции, имя функции и
переданные ей параметры в текстовый файл;
- декоратор, проверяющий типы, переданных декорируемой функции, аргументов.
- декоратор, который кэширует результат работы функции, тем самым обеспечивает
единственный вызов функции.
"""

from datetime import datetime

# декоратор, позволяющий вместе с результатом функции возвращать время ее работы


def decorator_time(func):

    def execution_time(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        return result, 'Время выполнения программы: {}'.format(end_time - start_time)

    return execution_time


@decorator_time
def my_func_1(a, b):
    return '{} + {} = {}'.format(a, b, a + b)


# декоратор, позволяющий записывать время работы функции,
# имя функции и переданные ей параметры в текстовый файл


def decorator_output_file(func):

    def execution_time(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        duration = datetime.now() - start_time

        with open('decorator.txt', 'a', encoding='utf-8') as f:
            print('Имя функции: {}'.format(func.__name__),
                  'Аргументы функции: {}'.format(args, kwargs),
                  'Время выполнения программы: {}'.format(duration),
                  sep=';\n', end='.\n\n', file=f)
        return result

    return execution_time


@decorator_output_file
def my_func_2(a, b):
    return a + b


# декоратор, проверяющий типы, переданных декорируемой функции, аргументов


def decorator_type(func):

    def type_arguments(*args, **kwargs):

        for arg in args:
            print(type(arg).__name__)

        for kwarg in kwargs.values():
            print(type(kwarg).__name__)

        result = func(*args, **kwargs)
        return result

    return type_arguments


@decorator_type
def my_func_3(a, b, c='qwerty'):
    return a, b, c


# декоратор, который кэширует результат работы функции, тем самым обеспечивает
# единственный вызов функции


def decorator_caching(func):
    dict_cache = {}

    def caching_result(*args):

        if args in dict_cache:
            return dict_cache[args]

        result = func(*args)
        dict_cache.update({args: result})
        return dict_cache[args]

    return caching_result


@decorator_caching
def my_func_4(a, b):
    return a + b
