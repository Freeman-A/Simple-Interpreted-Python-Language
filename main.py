import sys
from sipl_parser import siplParser
from lexxer import lexxer
from interpreter import evaluator


def read_file():
    """Reads the input file specified in the command line argument."""
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            input_str = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except UnicodeDecodeError:
        print('Error: UnicodeDecodeError')
        return

    tokens = lexxer(input_str)
    rpn_tokens = siplParser(tokens)
    result = evaluator(rpn_tokens)

    print("\n".join(map(str, result)))  # Convert each item in result to string


if __name__ == "__main__":
    read_file()
