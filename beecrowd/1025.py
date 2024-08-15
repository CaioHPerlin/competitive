def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            while mid > 0 and arr[mid - 1] == x:
                mid -= 1
            return mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

case_number = 1
results = []

while True:
    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break

    marbles = []

    for _ in range(n):
        marbles.append(int(input()))

    marbles.sort()

    results.append(f"CASE# {case_number}:")
    case_number += 1

    for _ in range(q):
        query = int(input())
        result = binary_search(marbles, query)
        if result != -1:
            results.append(f"{query} found at {result}")
        else:
            results.append(f"{query} not found")

[print(row) for row in results]
