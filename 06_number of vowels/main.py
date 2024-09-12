def number_of_vowels(message: str) -> int:
    """Return the number of vowels in the given message."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in message.lower() if char in vowels)


sentence = input("Enter a message: ")

print(number_of_vowels(sentence))
    