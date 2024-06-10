n = int(input())
blocks = list(map(int, input().split(' ')))

# default, default + 1, default + 2
# default + default + 1 + default + 2
# n * default + total_i
# n * default + total_i = total_blocks
# n * default = total_blocks - total_i
# default = (total_blocks - total_i) / n
 
total_blocks = sum(blocks)
total_i = sum(range(n))

default = (total_blocks - total_i) / n
remainder = (total_blocks - total_i) % n

if remainder != 0:
    print(-1)
    raise SystemExit(0)
    
staircase = []
for i in range(n):
    staircase.append(default + i)

count = 0
for i in range(n):
    diff = blocks[i] - staircase[i]
    if diff <= 0:
        count -= diff

print(int(count))