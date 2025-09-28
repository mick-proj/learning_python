#A short program that gives you the ASCII codes of a name until it received End.
while True:
    name = str(input())

    if name == 'End':
        break

    ascii_code_sum = 0
    for char in name:
        ascii_code_sum += ord(char)

    print(ascii_code_sum)