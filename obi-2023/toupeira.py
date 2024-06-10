s, t = map(int, input().split())

l = [0 for i in range(s)]
m = [l.copy() for i in range(s)]

for _ in range(t):
    a, b = map(int, input().split())
    m[a-1][b-1] = 1
    m[b-1][a-1] = 1

p = int(input())
count = p

for _ in range(p):
    path = list(map(int, input().split())) # index 0 = number of entries
    for i in range(1, path[0]):
        if m[path[i]-1][path[i+1]-1] == 0:
            count -= 1
            break

print(count)