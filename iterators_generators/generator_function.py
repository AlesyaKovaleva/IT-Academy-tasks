# def generator_function():
#     for x in range(5):
#         for y in range(3):
#             if (x + y) % 2 == 0: # если x + y делится нацело
#                 yield x * y
#
#
# generator = generator_function()
# for value in generator:
#     print(value)

# Либо можно это переписать так:
# Сокращенная запись подобных генераторов:


# generator = (x * y for x in range(5) for y in range(3) if (x + y) % 2 == 0)
# for value in generator:
#     print(value)

print(sum(x ** 2 for x in range(10)))