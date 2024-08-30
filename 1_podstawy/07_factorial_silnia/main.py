from functools import reduce


def sum_of_integers(n: int) -> int:
    """
    This function calculates the factorial of a given integer n.
    
    Args:
        n (int): The input number for which the factorial is to be calculated.
    
    Returns:
        int: The factorial of the input number n.
    """
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


print(sum_of_integers(0))
print(sum_of_integers(3))
print(sum_of_integers(5))
