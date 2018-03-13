from stack_0 import (push, pop, back, size, clear)


def test_push_0():
    stack = [1, 2, 3]
    push(stack, 42)
    if stack == [1, 2, 3, 42]:
        print('ok')
    else:
        print('not ok')


def test_push_1():
    stack = []
    push(stack, 42)
    if stack == [42]:
        print('ok')
    else:
        print('not ok')


def test_push_2():
    stack = [42] * 100
    if push(stack, 42) == 'Стэк переполнен.':
        print('ok')
    else:
        print('not ok')


def test_push_3():
    stack = [42] * 99
    push(stack, 42)
    if stack == [42] * 100:
        print('ok')
    else:
        print('not ok')


def test_pop_0():
    stack = [1, 2, 3]
    if pop(stack) == 3 and stack == [1, 2]:
        print('ok')
    else:
        print('not ok')


def test_pop_1():
    stack = []
    if pop(stack) == 'Стэк пуст':
        print('ok')
    else:
        print('not ok')


def test_pop_2():
    stack = [1]
    if pop(stack) == 1 and stack == []:
        print('ok')
    else:
        print('not ok')


def test_pop_3():
    stack = [1, 2, 3, 4, 100, 500, 42]
    if pop(stack) == 42 and stack == [1, 2, 3, 4, 100, 500]:
        print('ok')
    else:
        print('not ok')


def test_back_0():
    stack = [1, 2, 3]
    if back(stack) == 3:
        print('ok')
    else:
        print('not ok')


def test_back_1():
    stack = []
    if back(stack) == 'Стэк пуст':
        print('ok')
    else:
        print('not ok')


def test_back_2():
    stack = [-1]
    if back(stack) == -1:
        print('ok')
    else:
        print('not ok')


def test_back_3():
    stack = [1, 2, 3, 100, 500, 42]
    if back(stack) == 42:
        print('ok')
    else:
        print('not ok')


def test_size_0():
    stack = [1, 2, 3]
    if size(stack) == 3:
        print('ok')
    else:
        print('not ok')


def test_size_1():
    stack = []
    if size(stack) == 0:
        print('ok')
    else:
        print('not ok')


def test_size_2():
    stack = [0] * 50
    if size(stack) == 50:
        print('ok')
    else:
        print('not ok')


def test_size_3():
    stack = [0]
    if size(stack) == 1:
        print('ok')
    else:
        print('not ok')


def test_clear_0():
    stack = [1, 2, 3]
    clear(stack)
    if stack:
        print('not ok')
    else:
        print('ok')


def test_clear_1():
    stack = []
    clear(stack)
    if stack:
        print('not ok')
    else:
        print('ok')


def test_clear_2():
    stack = [0] * 50
    clear(stack)
    if stack:
        print('not ok')
    else:
        print('ok')


def test_clear_3():
    stack = [1]
    clear(stack)
    if stack:
        print('not ok')
    else:
        print('ok')


test_push_0()
test_push_1()
test_push_2()
test_push_3()
test_pop_0()
test_pop_1()
test_pop_2()
test_pop_3()
test_back_0()
test_back_1()
test_back_2()
test_back_3()
test_clear_0()
test_clear_1()
test_clear_2()
test_clear_3()
test_size_0()
test_size_1()
test_size_2()
test_size_3()
