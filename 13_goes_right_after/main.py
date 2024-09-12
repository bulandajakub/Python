def goes_after(word: str, first: str, second: str) -> bool:
    """
    Checks if the second letter comes after the first one in the given word.

    Args:
        word (str): The given word.
        first (str): The first letter.
        second (str): The second letter.

    Returns:
        bool: True if second comes after first, False otherwise.
    """
    if first and second in word and word.index(first) < word.index(second):
        indexes = [i for i, ltr in enumerate(word) if ltr == first]
        for index in indexes:
            if word[index + 1] == second:
                return True
    return False


assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
