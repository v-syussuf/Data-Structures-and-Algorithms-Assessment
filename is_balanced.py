def is_balanced(expression):
    stack = []

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or not is_matching(stack.pop(), char):
                return False

    return not stack

def is_matching(opening, closing):
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    return bracket_pairs[opening] == closing


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  
