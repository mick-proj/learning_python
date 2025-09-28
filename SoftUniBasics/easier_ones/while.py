total_sum = 0

while True:
    text = input()
    if text == 'NoMoreMoney':
        break
    current_num = float(text)

    if current_num >= 0:
        total_sum += current_num
        print(f'Increase: {current_num:.2f}')
    else:
        print('Invalid operation!')
        break

print(f"Total: {total_sum:.2f}")