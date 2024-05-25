import sys
from sll_interpreter import SLL_Interpreter


def run_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    interpreter = SLL_Interpreter()

    for line in lines:

        result = interpreter.interpret(line)
        if result is not None:
            print(result)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py <filename>')
    else:
        run_file(sys.argv[1])
