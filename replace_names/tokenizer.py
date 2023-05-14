import re

def tokenize(code: str) -> list[str]:
    return re.findall(r'\b\w+\b', code)
