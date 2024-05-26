import sys
from sipl_parser import siplParser
from lexxer import lexxer


def readFile():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            input_str = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    print("Lexing input...")
    tokens = lexxer(input_str)
    print("Tokens:")
    for token in tokens:
        print(token)

    print("Parsing tokens...")
    result = siplParser(tokens)
    print("Parsing result:")
    for token in result:
        print(token)


if __name__ == "__main__":
    readFile()
