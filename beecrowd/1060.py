arr = []

for _ in range(6):
    val = float(input())
    if  val > 0:
        arr.append(val)

print(f'{len(arr)} valores positivos')