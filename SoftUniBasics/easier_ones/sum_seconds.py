time_in_seconds_first = int(input())
time_in_seconds_second = int(input())
time_in_seconds_third = int(input())

total_time = int(time_in_seconds_first + time_in_seconds_second + time_in_seconds_third)

if total_time < 60:
    print(f'0:{total_time}')
else:
    minutes = total_time // 60
    seconds = total_time % 60
    if seconds < 10:
        print(f'{minutes}:0{seconds}')
    else:
        print((f'{minutes}:{seconds}'))