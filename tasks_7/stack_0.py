import sys


def push(stack, number):
    if len(stack) < 100:
        stack += [number]
        return 'ok'
    else:
        return 'Стэк переполнен.'


def pop(stack):
    if len(stack) == 0:
        return 'Стэк пуст'
    else:
        last_number = stack[-1]
        del stack[-1]
        return last_number


def back(stack):
    if len(stack) == 0:
        return 'Стэк пуст'
    else:
        last_number = stack[-1]
        return last_number


def size(stack):
    length = len(stack)
    return length


def clear(stack):
    stack[:] = []
    return 'ok'


commands = {
    'push': [push, 2],
    'pop': [pop, 1],
    'back': [back, 1],
    'size': [size, 1],
    'clear': [clear, 1],
}


def main():
    stack = []

    while True:
        command_input = input('Введите команду: ').lower().split()
        command = command_input[0]
        arguments = command_input[1:]

        if command == 'exit':
            print('bye')
            sys.exit()

        if command in commands:
            func, arg_count = commands[command]

            if arg_count == 1:
                print(func(stack))
            else:
                print(func(stack, arguments[0]))
        else:
            print('Такой команды не существует.')


if __name__ == '__main__':
    main()
