import math

n, l, d = map(int, input().split(' '))

liters = d * n / 1000
must_prepare = math.ceil(liters / l) * l

print(must_prepare)