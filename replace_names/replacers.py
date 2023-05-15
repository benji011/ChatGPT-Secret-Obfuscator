import keyword
from replace_names.tokenizer import tokenize
from replace_names.utils import read_ignored_keywords

def replace_names(code: str) -> str:
    tokens = tokenize(code)

    # Read ignored keywords from file
    ignored_keywords = read_ignored_keywords()

    # Create a mapping of old names to new names
    mapping = {}
    for token in tokens:
        if not token.isnumeric() and not token in keyword.kwlist and not token in ignored_keywords:
            mapping[token] = token[0] * len(token)

    # Replace old names with new names
    for old_name, new_name in mapping.items():
        code = code.replace(old_name, new_name)

    return code
