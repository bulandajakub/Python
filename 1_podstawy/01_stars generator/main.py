numbers = [2, 2, 2, 2, 5]


def stars_generator(user_list: list):
    generator = ('*' * num for num in user_list)

    for stars in generator:
        print(stars)


stars_generator(numbers)

# def stars_generator(user_list: list):
#     for num in user_list:
#         stars = ""
#         for _ in range(num):
#             stars += "*"
#         print(stars)
