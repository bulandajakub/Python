def replace_all(mainText: str, target: str, repl: str) -> str:
    replaced = mainText.replace(target, repl)
    return replaced

print(replace_all("Hello World", "World", "Python"))
