import random
secret_number = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")
for guesses_taken in range(1,7):
    print("Take a guess")
    guess = int(input('>'))
    if guess > secret_number:
        print("The guess is too high.")
    elif guess < secret_number:
        print("The guess is too low.")
    else:
        break

if guess == secret_number:
    print("Good job. You got it in " + str(guesses_taken) + " tries.")
else:
    print("Nope. Th number was " + str(secret_number) + " .")