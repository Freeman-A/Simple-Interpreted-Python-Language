# SIPL Interpreter

## Description
This is a Simple Interpreted Programming Language (SIPL) interpreter written in Python. It processes a given SIPL script file, tokenizes it, parses the tokens, and evaluates the expressions.

## Files
- `main.py`: Entry point of the interpreter. Reads the input file, tokenizes, parses, and evaluates it.
- `sipl_parser.py`: Contains the SIPL parser which converts token list to Reverse Polish Notation (RPN).
- `lexxer.py`: Contains the lexer which tokenizes the input string.
- `interpreter.py`: Contains the evaluator which processes the RPN tokens.
- `tokenizer.py`: Defines tokens and token types used in the language.
- `variable.py`: Defines the Variable class and global variable storage.
- `operators.py`: Contains functions for various operations used in the evaluator.

## Usage
To run the interpreter, use the following command:

## Replace `<filename>` with the path to your SIPL script file.

## Example

## python main.py <filename.sipl>

##This will read the `main.sipl` file, process it, and print the result of the script.
