"""
Задача 0
Реализовать класс лифта Elevator. Класс должен обладать методом, lift,
отвечающий за вызов лифта. При сложении/вычитании экземпляров класса должно
возвращаться значение производимой математической операции. Если производить
вычитание у лифта, который еще не совершал поднятий, должна быть выведена
ошибка неправильной операции. Предусмотреть возможность сравнения какой из
лифтов совершил большее количество поднятий.
Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
При строчных операциях необходимо вывести детальную информацию по лифту:
наименование, количество поднятий и процент от общего количества поднятий всех лифтов.
"""
import sys


class IncorrectOperation(Exception):
    pass


class Elevator:
    total_call = 0

    def __init__(self, name):
        self.name = name
        self.call = 0

    def lift(self):
        Elevator.total_call += 1
        self.call += 1

    def __add__(self, other):
        result = self.call + other.call
        return result

    def __sub__(self, other):

        if self.call < other.call:
            raise IncorrectOperation

        result = self.call - other.call
        return result

    def __gt__(self, other):
        result = self.call > other.call
        return result

    def __lt__(self, other):
        result = self.call < other.call
        return result

    def __eq__(self, other):
        result = self.call == other.call
        return result

    def __str__(self):

        if self.call == 0:
            percent = 0
        else:
            percent = round(self.call / Elevator.total_call * 100, 2)
        return '\nЛифт № {}\nКоличество поднятий: {}\nПроцент от общего количества поднятий всех лифтов: {}'\
            .format(self.name, self.call, percent)


class LiftManager:
    """
    Команды управления лифтами:

        lift  - вызвать лифты
        add   - сложить вызовы двух лифтов
        sub   - вычесть вызовы двух лифтов
        cmp   - сравнить кол-во вызовов двух лифтов
        all   - общее кол-во всех вызовов
        print - инфа о лифтах
        help  - список команд
        exit  - выход из программы

    Например: lift 1 2 3
    """
    def __init__(self, number_elevator):
        self.list_elevators = [Elevator(lift) for lift in range(1, number_elevator + 1)]

    def lift(self, arguments):
        if len(arguments) < 1:
            print('Введите номер лита для вызова.')

        for element in arguments:
            index = element - 1
            self.list_elevators[index].lift()

    def add(self, arguments):
        if len(arguments) != 2:
            print('Выберите два лифта.')
            return

        index1, index2 = arguments[0] - 1, arguments[1] - 1
        lift1, lift2 = self.list_elevators[index1], self.list_elevators[index2]
        result = lift1 + lift2
        print('Лифт № {} + Лифт № {} = {}'.format(lift1.name, lift2.name, result))

    def sub(self, arguments):
        if len(arguments) != 2:
            print('Выберите два лифта.')
            return

        index1, index2 = arguments[0] - 1, arguments[1] - 1
        lift1, lift2 = self.list_elevators[index1], self.list_elevators[index2]
        try:
            result = lift1 - lift2
            print('Лифт № {} - Лифт № {} = {}'.format(lift1.name, lift2.name, result))
        except IncorrectOperation:
            print('Невозможно выполнить операцию. У лифта № {} меньше вызовов чем у второго.'.format(lift1))

    def cmp(self, arguments):
        if len(arguments) != 2:
            print('Выберите два лифта.')
            return

        index1, index2 = arguments[0] - 1, arguments[1] - 1
        lift1, lift2 = self.list_elevators[index1], self.list_elevators[index2]

        if lift1 == lift2:
            print('У лифта № {} и у лифта № {} равное кол-во вызовов ({} раз(а))'
                  .format(lift1.name, lift2.name, lift1.call))
        elif lift1 > lift2:
            print('У лифта № {} большее кол-во вызовов ({} раз(а), чем у лифта № {} ({} раз(а))'
                  .format(lift1.name, lift2.call, lift2.name, lift2.call))
        elif lift1 < lift2:
            print('У лифта № {} меньшее кол-во вызовов ({} раз(а), чем у лифта № {} ({} раз(а))'
                  .format(lift1.name, lift2.call, lift2.name, lift2.call))

    def all_call(self, *args):
        print('Количество вызовов всех лифтов: {} раз(а)'.format(Elevator.total_call))

    def print_lift(self, arguments):
        for element in arguments:
            index = element - 1
            print(self.list_elevators[index])

    def help(self, *args):
        print(LiftManager.__doc__)

    commands = {
        'lift': lift,
        'add': add,
        'sub': sub,
        'cmp': cmp,
        'all': all_call,
        'print': print_lift,
        'help': help,
    }


def main():

    while True:
        try:
            number_elevator = int(input('Введите количество лифтов: '))
            break
        except ValueError:
            print("Вы ввели неверное значение.")

    manager = LiftManager(number_elevator)
    name = [lift.name for lift in manager.list_elevators]
    print('Ваши лифты:\n', '[' + '] ['.join(map(str, name)) + ']')
    manager.help()

    while True:
        command_input = input('Введите команду >> ').lower().split()

        if not command_input:
            continue

        command = command_input[0]

        try:
            arguments = list(map(int, command_input[1:]))
        except ValueError:
            print('Неправильно введён номер лифта.')
            continue

        if command == 'exit':
            sys.exit()

        if command in LiftManager.commands:
            func = LiftManager.commands[command]

            try:
                func(manager, arguments)
            except IndexError:
                print('Вы выбрали несуществующий лифт.')

        else:
            print('Такой команды не существует.')


if __name__ == '__main__':
    main()
