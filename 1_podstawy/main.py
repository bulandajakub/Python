def convert_emojis(input_message: str) -> str:
    """
    Convert emoticons in input message to their corresponding emojis.

    Args:
        input_message (str): The input message to be converted.

    Returns:
        str: The converted message with emoticons replaced by emojis.
    """
    emoji_dict = {
        ":)": "😊",
        ":(": "😔"
    }
    converted_message = ' '.join(
        emoji_dict.get(word, word) for word in input_message.split())
    return converted_message

text = input("Enter a message: ")
print(convert_emojis(text))
