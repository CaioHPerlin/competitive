total_seconds = int(input())

hours = total_seconds // 60 // 60
minutes = total_seconds // 60 % 60
seconds = total_seconds % 60

print(f'{hours}:{minutes}:{seconds}')