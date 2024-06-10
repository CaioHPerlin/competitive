# Entrada
# A primeira linha da entrada contém um número natural N representando o tipo do jogo de dominó: duplo-N.

# Saída
# Seu programa deve imprimir uma linha contendo um número natural representando quantas peças existem num jogo de dominó do tipo duplo-N.

# Restrições

# • 0 ≤ N ≤ 10000

N = int(input())
pieces = int(((N+1)*(N+2))/2)

print(pieces)