t = int(input())
res = ['' for _ in range(t)]
for test in range(t):
    n = int(input())
    students = list(input().split())
    freq = list(input().split())

    freq = [[char for char in reg if char != 'M'] for reg in freq]
    for i, student in enumerate(students):
        total = len(freq[i])
        attendance = freq[i].count('P') / total
        if attendance < 0.75:
            res[test] += f'{student} '

[print(line.strip()) for line in res]

