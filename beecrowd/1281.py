n = int(input())
res = []

for _ in range(n):
    m = int(input())

    products = {}
    for _ in range(m):
        produto, price = input().split()
        products[produto] = float(price)
    
    p = int(input())
    
    sum = 0.0
    for _ in range(p):
        item, amount = input().split()
        amount = int(amount)
        sum += products[item] * amount
    
    res.append(f'R$ {sum:.2f}')

[print(row) for row in res]