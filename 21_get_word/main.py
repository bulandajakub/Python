import re

def get_word(text: str, index: int) -> str:
    """
    Returns the word at the specified index in the given text.

    Args:
        text (str): The input string to extract the word from.
        index (int): The index of the word to return, starting from 1.

    Returns:
        str: The word at the specified index, or "there is no such index"
             if the index is out of bounds.
    """
    word_list = re.findall(r"[a-zA-Z']+", text)
    return word_list[index - 1] if 0 <= index - 1 < len(word_list) else "there is no such index"


text = 'Hello there, whats up?'
print(get_word(text, 0))
print(get_word(text, 1))
print(get_word(text, 2))
print(get_word(text, 3))
print(get_word(text, 4))
print(get_word(text, 5))
