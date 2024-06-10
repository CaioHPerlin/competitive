n = int(input())
m = int(input())

bought = []
for i in range(m):
    bought.append(int(input()))
bought = list(set(bought))

print(n - len(bought))