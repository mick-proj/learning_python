my_pets = ['Sophie', 'Zoey', 'Joey']
while True:
    print('Enter a name:')
    name = input()
    if name not in my_pets:
        if name == 'stop':
            break
        print("I don't have a pet named " + name)
    else:
        print(name + ' is my pet')