numbers = [2, 3, 4, 7, 5]


def maximum_number(number_list: list[float]) -> float:
    max_number = number_list[0]

    for number in number_list:
        if number > max_number:
            max_number = number

    return max_number


# def max_number(number_list: list[float]) -> float:
#     return max(number_list)

print(maximum_number(numbers))
