v = int(input())

a = int(input())
f = int(input())
p = int(input())

bills = sorted([a, f, p])

count = 0

for bill in bills:
    if(v >= bill):
        v -= bill
        count += 1

print(count)