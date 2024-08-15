def can_reorder(n, order):
    pile = []
    current = 1
    for wagon in order:
        while current <= n and (len(pile) == 0 or pile[-1] != wagon):
            pile.append(current)
            current += 1
        if pile[-1] == wagon:
            pile.pop()
        else:
            return "No"
    return "Yes"

output = []

while True:
    n = int(input().strip())
    if n == 0:
        break
    
    block_res = []
    
    while True:
        line = input().strip()
        if line == '0':
            break
        order = list(map(int, line.split()))
        res = can_reorder(n, order)
        block_res.append(res)
    
    output.append('\n'.join(block_res))
    output.append('')

[print(line) for line in output]
