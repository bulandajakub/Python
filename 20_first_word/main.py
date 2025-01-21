import re


def first_word(text: str) -> str:
    """
    Returns the first word in a given text.

    The function uses regular expression to search for the first sequence of
    alphabetic characters in the given text. The search is case-insensitive.

    Args:
        text (str): The input string to be processed.

    Returns:
        str: The first word in the input string, or an empty string if no words
        are found.
    """
    # re.search searches for the first occurrence of a pattern in the string
    # and returns a match object if a match is found, otherwise None.
    # The pattern [a-zA-Z']+ searches for one or more alphabetic characters
    # The match object contains the matched text, which can be accessed with the
    # .group() method.
    match = re.search(r"[a-zA-Z']+", text)
    return match.group(0) if match else ""


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
