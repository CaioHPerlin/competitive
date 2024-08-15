n = int(input())

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decode(enc, shift):
    dec = ''
    for char in enc:
        dec += letters[(letters.index(char) - shift) % 26]
    return dec

res = []
for _ in range(n):
    enc = input().strip()
    shift = int(input())
    res.append(decode(enc, shift))

[print(line) for line in res]