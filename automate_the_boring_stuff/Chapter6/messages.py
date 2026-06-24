import random
import sys

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
   

def main():
    while True:
        print('Ask a yes or no question:')
        question = input('> ')

        if question.lower() == 'exit':
            print('Goodbye!')
            return

        print(random.choice(messages))

if __name__ == "__main__":
    main()