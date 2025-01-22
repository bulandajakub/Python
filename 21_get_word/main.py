import re

def get_word(text: str, position: int) -> str:
    """Returns the word at the given position in the given text.

    Args:
        text (str): The input string to extract the word from.
        position (int): The position of the word to return.

    Returns:
        str: The word at the given position, or "there is no such position" if position
            is out of bounds.
    """
    words = re.findall(r"[a-zA-Z']+", text)
    return words[position] if position < len(words) else "there is no such position"


text = 'Hello there, whats up?'
print(get_word(text, 0))
print(get_word(text, 1))
print(get_word(text, 2))
print(get_word(text, 3))
print(get_word(text, 4))
