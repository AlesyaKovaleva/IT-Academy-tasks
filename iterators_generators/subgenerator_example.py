def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():
    yield '[generator]    start'
    yield from subgenerator()
    yield '[generator]    end'


for value in generator():
    print(value)

