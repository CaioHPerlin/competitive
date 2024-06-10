n = int(input())
print(n)

bills100 = n // 100

n %= 100

bills50 = n // 50

n %= 50

bills20 = n // 20

n %= 20

bills10 = n // 10

n %= 10

bills5 = n // 5

n %= 5

bills2 = n // 2

n %= 2

bills1 = n

print(f'{bills100} nota(s) de R$ 100,00')
print(f'{bills50} nota(s) de R$ 50,00')
print(f'{bills20} nota(s) de R$ 20,00')
print(f'{bills10} nota(s) de R$ 10,00')
print(f'{bills5} nota(s) de R$ 5,00')
print(f'{bills2} nota(s) de R$ 2,00')
print(f'{bills1} nota(s) de R$ 1,00')

# 576
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00 