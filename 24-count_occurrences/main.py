import re

def count_occurrences(main_str: str, sub_str: str) -> int:
  """Counts the number of (possibly overlapping) occurrences of a substring within a main string,
    ignoring case.

    This function uses regular expressions with a positive lookahead assertion to find
    all occurrences of `sub_str` in `main_str`, even when they overlap. The search
    is case-insensitive.

    Args:
        main_str: The main string to search within.
        sub_str: The substring to search for. Must not be an empty string.

    Returns:
        The total number of occurrences of `sub_str` in `main_str`.

    Examples:
        >>> count_occurrences("hello world hello", "hello")
        2
        >>> count_occurrences("Hello World hello", "hello")
        2
        >>> count_occurrences("appleappleapple", "appleapple")
        2
        >>> count_occurrences("HELLO", "hello")
        1
    """
    # re.IGNORECASE makes the search case-insensitive
    # The '(?={})' is a positive lookahead assertion.
    # It finds matches without consuming the characters, allowing overlaps.
    # re.escape() is used to escape any special characters in the sub_str
    # so they are treated literally by the regex engine.
  return len(re.findall(f"(?={re.escape(sub_str.lower())})", main_str.lower()))
