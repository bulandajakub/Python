def replace_all(mainText: str, target: str, repl: str) -> str:
    """Replaces all occurrences of target string in mainText with repl string.
    
    Args:
        mainText (str): The string in which to replace the target.
        target (str): The string to replace.
        repl (str): The string to use for replacement.
    
    Returns:
        str: The new string with the replacements made.
    """
    return mainText.replace(target, repl)
