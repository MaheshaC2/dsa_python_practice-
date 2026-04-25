# Problem: Min Stack
# Category: Stack
# Time Complexity: O(1)
# Space Complexity: O(n)

stack = []
min_stack = []

def push(x):
    stack.append(x)
    if not min_stack or x <= min_stack[-1]:
        min_stack.append(x)

def pop():
    if stack[-1] == min_stack[-1]:
        min_stack.pop()
    stack.pop()

def get_min():
    return min_stack[-1]

push(3)
push(5)
push(2)
push(1)

print("Min:", get_min())
