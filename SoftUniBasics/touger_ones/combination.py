num = int(input())
solves = 0

for x in range(num+1):
    for y in range(num+1):
        for z in range(num+1):
            if x + y + z == num:
                solves += 1

print(solves)