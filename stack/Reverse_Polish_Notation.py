# Problem: Evaluate Reverse Polish Notation
# Category: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def eval_rpn(tokens):
    stack = []

    for token in tokens:

        if token not in "+-*/":
            stack.append(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)

            elif token == "-":
                stack.append(a - b)

            elif token == "*":
                stack.append(a * b)

            else:
                stack.append(int(a / b))

    return stack[0]
