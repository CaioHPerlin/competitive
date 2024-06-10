# total_seconds = int(input())

# hours = total_seconds // 60 // 60
# minutes = total_seconds // 60 % 60
# seconds = total_seconds % 60

# print(f'{hours}:{minutes}:{seconds}')

total_days = int(input())

years = total_days // 365
months = total_days % 365 // 30
days = total_days % 365 % 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')