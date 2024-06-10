n = int(input())
res = []

for _ in range(n):
    occur = input().split(' ')
    t, h = int(occur[0]), int(occur[1][0])
    
    if t > 45:
        add = t - 45
        res.append(f'{45 * h}+{add}')
    else:
        res.append(f'{t + 45 * (h - 1)}')

print('\n'.join(res))