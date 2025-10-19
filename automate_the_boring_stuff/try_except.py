def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: cannot divide by zero')
print(spam(divide_by=2))
print(spam(divide_by=12))
print(spam(divide_by=0))
print(spam(divide_by=1))