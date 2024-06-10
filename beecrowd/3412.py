n = int(input())
for i in range(n):
    res = 0
    name = input()
    grades = list(map(float, input().split(' ')))
    match len(grades):
        case 1:
            res = f'{name}: {(grades[0] / 2):.1f}'
        case 2:
            res = f'{name}: {((grades[0] + grades[1]) / 2):.1f}'
        case 3:
            res = f'{name}: {((grades[0] + grades[1] + grades[2]) / 3):.1f}'
        case 4:
            if grades[3] > min(grades):
                grades[grades.index(min(grades))] = grades[3]
            res = f'{name}: {((grades[0] + grades[1] + grades[2]) / 3):.1f}'
    print(res)
