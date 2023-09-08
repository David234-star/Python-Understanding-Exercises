class OperatorPrecedenceParser:
    def __init__(self):
        self.stack = []
        self.precedence = {}

    def set_operators(self, operators):
        self.precedence = operators

    def parse_expression(self, expression):
        tokens = self.tokenize(expression)

        for token in tokens:
            if token.isdigit():
                print(token, end=' ')
            elif token in self.precedence:
                while self.stack and self.precedence.get(self.stack[-1], 0) >= self.precedence[token]:
                    print(self.stack.pop(), end=' ')
                self.stack.append(token)
            elif token == '(':
                self.stack.append(token)
            elif token == ')':
                while self.stack and self.stack[-1] != '(':
                    print(self.stack.pop(), end=' ')
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()

        while self.stack:
            print(self.stack.pop(), end=' ')

        print()

    def tokenize(self, expression):
        tokens = []
        current_token = ''

        for char in expression:
            if char.isdigit():
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                tokens.append(char)

        if current_token:
            tokens.append(current_token)

        return tokens


# Example usage

parser = OperatorPrecedenceParser()

# Set operators and precedence levels
operators = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}
parser.set_operators(operators)

# Get expression from user
expression = input("Enter an expression: ")

# Parse and print the expression
parser.parse_expression(expression)
