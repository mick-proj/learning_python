from code import interact


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    requested_number = int(input())

    while requested_number != 1:
        print(requested_number)
        requested_number = collatz(requested_number)

    print(requested_number)
except ValueError:
    print("Expected input is an integer")