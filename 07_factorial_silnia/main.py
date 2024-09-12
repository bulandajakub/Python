from functools import reduce


def factorial(n: int) -> int:
    """
    This function calculates the factorial of a given integer n.
    
    Args:
        n (int): The input number for which the factorial is to be calculated.
    
    Returns:
        int: The factorial of the input number n.
    """
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
    # return n*factorial(n-1) if n > 1 else 1


print(factorial(0))
print(factorial(3))
print(factorial(5))
