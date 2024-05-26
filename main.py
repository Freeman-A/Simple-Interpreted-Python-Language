import sys
from sipl_parser import siplParser
from lexxer import lexxer
from interpreter import evaluator


def readFile():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
            input_str = file.read()
            print("Input string read from file:")
            print(input_str)  # Print the input string for debugging
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except UnicodeDecodeError:
        print('ERROR ENCOUNTERED: UnicodeDecodeError')
        return

    print("Lexing input...")
    tokens = lexxer(input_str)

    print("Parsing tokens...")
    rpn_tokens = siplParser(tokens)

    print("Evaluating tokens...")
    result = evaluator(rpn_tokens)

    print("Evaluation result:")
    print(result)


if __name__ == "__main__":
    readFile()
