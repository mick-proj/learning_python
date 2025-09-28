for hour in range(24):
    for minutes in range(60):
        for seconds in range(60):
            if minutes < 10:
                if seconds < 10:
                    print(f'{hour}:0{minutes}:0{seconds}')
                else:
                    if minutes < 10:
                        print(f'{hour}:0{minutes}:{seconds}')
                    else:
                        print(f'{hour}:{minutes}:{seconds}')
            else:
                if seconds < 10:
                    print(f'{hour}:{minutes}:0{seconds}')
                else:
                    print(f'{hour}:{minutes}:{seconds}')
#The following if clauses make the program stop at 1 o'clock.
            if hour == 1:
                break
        if hour == 1:
            break
    if hour == 1:
        break