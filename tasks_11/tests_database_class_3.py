from database_class_3 import (BaseDB, TextDB, JsonDB, Student, make_list_student)


class DBTests:

    classname = None
    filename = None

    def __init__(self, classname, filename):
        if classname is None or filename is None:
            raise NotImplementedError

        self.classname = classname
        self.filename = filename

    def run(self):
        self.test_load_ok()
        self.test_load_not_ok()
        self.test_find_ok()

    def test_load_ok(self):
        obj = self.classname(self.filename)

        assert len(obj.db) == 5, 'Not Ok'
        assert type(obj.db[0]) == Student, 'Not Ok'
        assert obj.db[0].values() == ['Петр', 'Петров', 'мужской', '23'], 'Not Ok'
        print('Ok')

    def test_load_not_ok(self):
        try:
            obj = self.classname('Non_existing.file')
            print('Not Ok')
        except FileNotFoundError:
            print('Ok')

    def test_find_ok(self):
        obj = self.classname(self.filename)
        search = obj.find(['23'])
        assert len(search) == 1, 'Not Ok'
        id, student = search[0]
        assert id == 1, 'Not Ok'
        assert student.values() == ['Петр', 'Петров', 'мужской', '23'], 'Not Ok'
        print('Ok')


def test_make_list_student_ok():
    txt_obj = make_list_student('my_file.txt')
    assert type(txt_obj) == TextDB, 'Not Ok'

    json_obj = make_list_student('my_file.json')
    assert type(json_obj) == JsonDB, 'Not Ok'
    print('Ok')


def test_make_list_student_not_ok():
    obj = make_list_student('Non_existing.file')
    assert obj is None, 'Not Ok'
    print('Ok')


def main():
    text_db_tests = DBTests(TextDB, 'my_file.txt')
    text_db_tests.run()
    print()
    json_db_tests = DBTests(JsonDB, 'my_file.json')
    json_db_tests.run()
    print()
    test_make_list_student_ok()
    test_make_list_student_not_ok()


if __name__ == '__main__':
    main()
