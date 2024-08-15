def get_diamonds(s):
    count = 0
    stack = 0
    
    for char in s:
        if char == '<':
            stack += 1
        elif char == '>' and stack > 0:
            count += 1
            stack -= 1
            
    return count

n = int(input().strip())
res = []
for _ in range(n):
    line = input().strip()
    res.append(get_diamonds(line))

[print(row) for row in res]
