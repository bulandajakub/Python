from itertools import zip_longest

def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    """
    Checks if the number of differing characters between two strings is within a threshold.

    This includes character mismatches and any extra characters in the longer string.
    Characters are compared pairwise using zip_longest, which fills missing values with None.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        threshold (int): Maximum allowed number of differences.

    Returns:
        bool: True if the number of differences is less than or equal to the threshold.

    Example:
        fuzzy_string_match("cat", "car", 1) → True
        fuzzy_string_match("apple", "apples", 0) → False
    """
    return sum(a != b for a, b in zip_longest(str1, str2)) <= threshold


"""
0.5 seconds  # a != b
1.0 seconds  # operator.ne(a, b)
Use a != b unless you need to pass the comparison as a function.
Prefer operator.ne in functional constructs like map(op.ne, list1, list2) or starmap(op.ne, iterable)
"""

print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
