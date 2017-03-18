def is_matched(expression):
    bracket_dict ={'{':'}', '[':']', '(':')'}
    stack = []
    for char in expression:
        if char in bracket_dict:
            stack.append(bracket_dict[char])
        else:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                return False
    return len(stack) == 0


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
