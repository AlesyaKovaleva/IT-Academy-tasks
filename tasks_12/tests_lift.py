from lift import (Elevator, LiftManager, main, IncorrectOperation)


class LiftTests:

    def run(self):
        self.total_call_ok()
        self.lift_ok()
        self.add_ok()
        self.sub_ok()
        self.sub_not_ok()
        self.gt_ok()
        self.lt_ok()

    def total_call_ok(self):
        lift1 = Elevator(1)
        lift2 = Elevator(2)

        for _ in range(30):
            lift1.lift()
        for _ in range(12):
            lift2.lift()

        if Elevator.total_call == 42:
            print('Test Ok')
        else:
            print('Test not Ok')

    def lift_ok(self):
        lift1 = Elevator(1)
        lift2 = Elevator(2)

        for _ in range(10):
            lift1.lift()
        for _ in range(5):
            lift2.lift()

        if lift1.call == 10 and lift2.call == 5:
            print('Test Ok')
        else:
            print('Test not Ok')

    def add_ok(self):
        lift1 = Elevator(1)
        lift2 = Elevator(2)

        for _ in range(10):
            lift1.lift()
        for _ in range(5):
            lift2.lift()

        if lift1 + lift2 == 15:
            print('Test Ok')
        else:
            print('Test not Ok')

    def sub_ok(self):
        lift1 = Elevator(1)
        lift2 = Elevator(2)

        for _ in range(10):
            lift1.lift()
        for _ in range(5):
            lift2.lift()

        if lift1 - lift2 == 5:
            print('Test Ok')
        else:
            print('Test not Ok')

    def sub_not_ok(self):
        lift1 = Elevator(1)
        lift2 = Elevator(2)

        for _ in range(5):
            lift2.lift()
        try:
            result = lift1 - lift2
            print('Test not Ok', result)
        except IncorrectOperation:
            print('Test Ok')

    def gt_ok(self):
        lift1 = Elevator(1)
        lift2 = Elevator(2)

        for _ in range(10):
            lift1.lift()
        for _ in range(5):
            lift2.lift()

        if lift1 > lift2:
            print('Test Ok')
        else:
            print('Test not Ok')

    def lt_ok(self):
        lift1 = Elevator(1)
        lift2 = Elevator(2)

        for _ in range(5):
            lift1.lift()
        for _ in range(10):
            lift2.lift()

        if lift1 < lift2:
            print('Test Ok')
        else:
            print('Test not Ok')

    def eq_ok(self):
        lift1 = Elevator(1)
        lift2 = Elevator(2)

        for _ in range(10):
            lift1.lift()
        for _ in range(10):
            lift2.lift()

        if lift1 == lift2:
            print('Test Ok')
        else:
            print('Test not Ok')


lift = LiftTests()
LiftTests.run(lift)
