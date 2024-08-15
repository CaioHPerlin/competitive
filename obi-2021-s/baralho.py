#    1  2  3  4
#  C 0, 0, 0, 0,
#  E 0, 0, 0, 0,
#  O 0, 0, 0, 0,
#  P 0, 0, 0, 0,

# m[row, col]
m = [[0 for j in range(0, 13)] for i in range(0, 4)]

card_string = input()
cards = [card_string[i:i+3] for i in range(0, len(card_string), 3)]

res = [0 for i in range(0, 4)]

for card in cards:
    row = 0

    if card[2] == 'E':
        row = 1
    if card[2] == 'O':
        row = 2
    if card[2] == 'P':
        row = 3
    
    m[row][int(card[0:2])-1] += 1

    # if (m[row][int(card[0:2])-1] > 1):
    #     res[row] = 'erro'

for x in m:
    print(x)