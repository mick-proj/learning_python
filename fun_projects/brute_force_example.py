import itertools

def brute_force_pin():
    digits = '0123456789'

    pin_combinations = itertools.product(digits, repeat = 6)

    correct_pin = '332211'

    attempts = 0

    for pin in pin_combinations:
        attempts += 1
        pin_str = ''.join(pin)

        if pin_str == correct_pin:
            print(f'Brute force successful! Pin is {pin_str}')
            print(f'Total attempts: {attempts}')
            return

brute_force_pin()