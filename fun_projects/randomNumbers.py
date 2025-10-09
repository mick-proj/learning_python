import random
name = ["Luke", "Miro", "Stef", "Jordan", "Meshi", "Stefano", "Steve"]
for i in range(len(name)):
    print(f'{name[i]} got number {random.randint(1,100)}')