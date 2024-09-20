def max_digit(value: int) -> int:
    """
    Given an integer value, this function returns the maximum digit in the integer.

    Parameters:
        value (int): The integer value for which to find the maximum digit.

    Returns:
        int: The maximum digit in the given integer.
    """
    return int(max(list(str(value))))
    # return max(map(int, str(number)))
