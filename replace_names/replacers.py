import keyword
from replace_names.tokenizer import tokenize

def replace_names(code: str) -> str:
    tokens = tokenize(code)

    # Create a mapping of old names to new names
    mapping = {}
    for token in tokens:
        if not token.isnumeric() and not token in keyword.kwlist:
            mapping[token] = token[0] * len(token)

    # Replace old names with new names
    for old_name, new_name in mapping.items():
        code = code.replace(old_name, new_name)

    return code
