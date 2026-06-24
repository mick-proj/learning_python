import copy

spam = ['A', 'B', 'C']
cheese = copy.copy(spam)
cheese[1] = 42
print(cheese)