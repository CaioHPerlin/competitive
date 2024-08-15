h, a, b = map(int, input().split())

pi = 3

if a**2 + b**2 != h**2:
    print('Nao eh retangulo!')
    raise SystemExit;

triangle = a * b / 2
circle = (pi * (b / 2)**2) / 2
area = int(triangle + circle)

print(f'AREA = {area}')