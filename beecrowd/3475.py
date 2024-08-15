num_to_text = [
    "zero",
    "um",
    "dois",
    "tres",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove"
]

str = input()

if str.isdigit():
    print(num_to_text[int(str)])
else:
    print(num_to_text.index(str))
