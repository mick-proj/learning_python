import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

# Random password of length 10
password_length = 10
random_password = ''

for _ in range(password_length):
    random_password += random.choice(characters)

print('Randomly Generated Password: ', random_password)