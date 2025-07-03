def translation(text: str) -> str:
    """Translate given text from "triple vowel" language to English.

    This function works by iterating through the given text and appending
    characters to the result list. If a character is a vowel, it is added to
    the result list and the next 2 characters are skipped. If a character is
    not a vowel, it is added to the result list and the next character is
    skipped. If the character is a space, it is added to the result list and
    no characters are skipped.

    The function then returns the result list joined into a string.

    Args:
        text (str): The text to translate.

    Returns:
        str: The translated text.
    """
    vowels = set("aeiouy") # using set for O(1) lookup
    result = []
    append = result.append # local lookup optimization
    i = 0
    
    while i < len(text):
        char = text[i]
        append(char)
        i += 3 if char in vowels else 2 if char != ' ' else 1
    return ''.join(result)

    # second
    # import re,functools
    # translate=functools.partial(re.sub,r"(\w)(\1\1|.)",r"\1")
    
    # third
    # translate=lambda s:s and s[0]+translate(s[1+(s[0]!=' ')+(s[0]in'aeiouy'):])


print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")