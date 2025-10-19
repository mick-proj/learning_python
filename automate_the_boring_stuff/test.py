import random

num_input = int(input('How many random numbers from 1 to 10 do you want? '))

def get_random_dice_roll():
        random_number = random.randint(1, 10)
        return random_number

for i in range(num_input):
    print(get_random_dice_roll())
