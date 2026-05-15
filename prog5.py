# Expression evaluation using stack (postfix)
def evaluate_postfix(expression):
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.append(result)
    
    return stack[0] if stack else 0

# Example usage
expression = input("Enter a postfix expression (e.g., '3 4 + 2 *'): ")
result = evaluate_postfix(expression)
print("Result:", result)