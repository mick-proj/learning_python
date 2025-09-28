sum = []

for _ in range(2):
    first_num = int(input())
    second_num = int(input())

    sum.append(first_num + second_num)

if sum[0] == sum[1]:
    print(f'Yes, sum = {sum[0]}')
else:
    difference = abs(abs(sum[0]) - abs(sum[1]))
    print(f'No, diff = {difference}')
