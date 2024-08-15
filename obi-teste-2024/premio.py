p = int(input())
d = int(input())
b = int(input())

score = p + (d*2) + (b*3)

if score >= 150:
    print('B')
elif score >= 120:
    print('D')
elif score >= 100:
    print('P')
else:
    print('N')