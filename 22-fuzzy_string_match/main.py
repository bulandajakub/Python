def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
  """
  Checks if the number of differing characters between two strings is within a given threshold.

    This function compares two strings character-by-character and counts how many positions
    have different characters. It returns True if the count of differing characters is
    less than or equal to the specified threshold; otherwise, it returns False.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        threshold (int): The maximum number of allowed differing characters.

    Returns:
        bool: True if the number of differences is less than or equal to the threshold, False otherwise.
  """
  return sum(a != b for a, b in zip(str1, str2)) <= threshold


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
