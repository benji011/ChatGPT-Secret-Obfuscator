def read_file(filepath: str) -> str:
    with open(filepath, 'r') as f:
        return f.read()

def read_ignored_keywords():
    with open("keywords.txt", 'r') as f:
        return [line.strip() for line in f]