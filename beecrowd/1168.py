n = int(input())
nums = [input().strip() for _ in range(n)]

num_to_led = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for num in nums:
    leds = 0
    for char in num:
        leds += num_to_led[int(char)]
    print(f'{leds} leds')

# depois descobri a função sum, que tornaria esse código mais eficiente da seguinte forma:
# for num in nums:
#     leds = sum(num_to_led[int(char)] for char in num)
#     print(f'{leds} leds')


