b = int(input())
t = int(input())
bill = 160 * 70
felix = (b+t)*70/2

def output():
    if felix > bill/2:
        return 1
    if felix < bill/2:
        return 2
    return 0

print(output())