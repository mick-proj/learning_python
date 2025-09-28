import sys

number_of_lines = int(input())

max_num = -sys.maxsize # maxsize = 9223372036854775807
min_num = sys.maxsize

for _ in range(number_of_lines):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num
    if current_num < min_num:
        min_num = current_num

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')