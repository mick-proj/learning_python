count = int(input())
odds_sum = 0
even_sum = 0

for i in range(count):
    current_num = int(input())
    if i % 2 == 0:
        even_sum += current_num
    else:
        odds_sum += current_num

if even_sum == odds_sum:
    print(f'Yes, Sum = {even_sum}')
else:
    print(f'No, Diff = {abs(abs(even_sum) - abs(odds_sum))}')