n = int(input())
print(n)

bills = [100, 50, 20, 10, 5, 2, 1]

for value in bills:
    amount = n // value
    print(f'{amount} nota(s) de R$ {value},00')
    n %= value

# 576
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00 