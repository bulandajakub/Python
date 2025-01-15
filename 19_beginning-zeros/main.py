def beginning_zeros(a: str) -> int:
    """Returns the number of leading zeros in the input string.

    Args:
        a (str): The input string to count leading zeros.

    Returns:
        int: The number of leading zeros in the input string.
    """
    # Calculate the difference in length before and after stripping leading zeros
    return len(a) - len(a.lstrip('0'))


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
