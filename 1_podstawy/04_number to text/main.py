nums = input('Phone number: ')

# for num in nums:
#     print(numbers_mapped.get(num))


def convert_numbers_to_text(phone_numbers):
    """
    Convert a string of phone numbers to their corresponding text representation.

    Args:
        phone_numbers (str): A string of phone numbers.

    Returns:
        str: The text representation of the phone numbers.
    """

    # Map numbers to their corresponding text representation
    numbers_mapping = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    # Get the text representation of each number in the phone number string
    numbers_text = [numbers_mapping.get(num) for num in phone_numbers]

    # Join the text representation of each number with a space
    numbers_text_joined = ' '.join(numbers_text)

    return numbers_text_joined


print(convert_numbers_to_text(nums))
