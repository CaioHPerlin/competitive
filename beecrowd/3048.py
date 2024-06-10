n = int(input())

seq = []
for i in range(n):
    seq.append(int(input()))

res = 0

prev = 0
for i in seq:
    if(i != prev):
        res += 1
    prev = i

print(res)