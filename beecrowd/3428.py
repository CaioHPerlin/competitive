# balões
# n baloes
# h0 h1 h2 ... hn

n = int(input())
b = list(map(int, input().split()))

m = [[0 for j in range(n)] for i in range(n)]

for x in range(n):
    y = n - b[x]
    m[y][x] = 1

arrows = 0
for y in range(n):
    h = y
    isPath = False
    for x in range(n): # verify shot
        if h >= n:
            if isPath:
                arrows += 1
            break
        if m[h][x] == 1:
            m[h][x] = 0
            isPath = True
            h += 1
        if isPath and x == n - 1:
            arrows += 1 # shoot

print(arrows)
