def between_markers(text: str, start: str, end: str) -> str:
    """
    Returns the substring between two markers in a given string.

    Args:
        text (str): The string to be processed.
        start (str): The starting marker.
        end (str): The ending marker.

    Returns:
        str: The substring between the two markers.
    """
    # Find the positions of the markers in the string
    start_index = text.find(start)
    end_index = text.find(end)

    # If the markers are not found, return an empty string
    if start_index == -1 or end_index == -1:
        return ""
    # If the markers are found, return the substring between them
    else:
        return text[start_index + len(start):end_index]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")
