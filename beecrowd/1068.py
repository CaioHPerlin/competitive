res = []

while True:
    try:
        line = input().strip()
        if not line:
            break
        stack = []
        result = "correct"
        for char in line:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    result = "incorrect"
                    break
                stack.pop()
        if stack:
            result = "incorrect"
        res.append(result)
    except EOFError:
        break

[print(row) for row in res]