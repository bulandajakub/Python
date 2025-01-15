def three_words(text: str) -> bool:
    """Check if a string contains three consecutive words.

    Args:
        text (str): The input string to be checked.

    Returns:
        bool: True if the string contains three consecutive words, False otherwise.
    """
    count = 0
    # Split the input text into words and iterate over them
    for word in text.split():
        # Increment count if the word is alphabetic, otherwise reset to 0
        count = count + 1 if word.isalpha() else 0
        # Return True if there are three consecutive alphabetic words
        if count == 3:
            return True
    # Return False if no three consecutive words are found
    return False

    # Second solution
    # return True if re.search('\D+\s\D+\s\D+', words) else False


# These "asserts" are used for self-checking
assert three_words("Hello World hello") == True
assert three_words("He is 123 man") == False
assert three_words("1 2 3 4") == False
assert three_words("bla bla bla bla") == True
assert three_words("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
