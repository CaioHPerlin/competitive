d = int(input())

def points():
    if d <= 800:
        return 1
    
    if d <= 1400:
        return 2

    return 3
    
print(points())