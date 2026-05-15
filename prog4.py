# Parenthesis checking using stack



def is_balanced(expression):
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    
    return not stack

# User input
expression = input("Enter an expression to check for balanced parentheses: ")
print(is_balanced(expression))