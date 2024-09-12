numbers = [2, 3, 4, 7, 5, 2]


def remove_duplicates(elements: list) -> list:
    new = []

    for element in elements:
        if element not in new:
            new.append(element)

    return new


# for number in numbers:
#     if numbers.count(number) > 1:
#         numbers.remove(number)


print(remove_duplicates(numbers))
