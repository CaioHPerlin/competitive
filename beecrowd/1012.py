A, B, C = map(float, input().split(' '))

triangle = A * C / 2
circle = 3.14159 * C**2
trap = ((A + B) * C) / 2
square = B**2
rectangle = A * B

print(f'TRIANGULO: {triangle:.3f}')	
print(f'CIRCULO: {circle:.3f}')	
print(f'TRAPEZIO: {trap:.3f}')	
print(f'QUADRADO: {square:.3f}')	
print(f'RETANGULO: {rectangle:.3f}')

# TRIANGULO: 7.800
# CIRCULO: 84.949
# TRAPEZIO: 18.200
# QUADRADO: 16.000
# RETANGULO: 12.000 