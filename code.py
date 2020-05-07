from sys import exit
from random import shuffle

file = open("example.txt", "r")
lines = file.readlines()
file.close()

it = 0
iter = len(lines) // 8
x = 0

print(iter)

for it in range(iter):
    #Exercise: easy x 4
    for i in range(4):
        print("- Exercise: easy")
        print("  Terms:")
        print("  - " + lines[i*2+x].strip())
        print("  - " + lines[i*2+1+x].strip())

    # Exercise: four_one x 2
    for i in range(2):
        print("- Exercise: four_one")
        print("  Terms:")
        list = lines[i*4+x:i*4+4+x]
        shuffle(list)

        for line in list:
            print("  - " + line.strip())

    # Exercise: identify_image x 2
    for i in range(2):
        print("- Exercise: identify_image")
        print("  Terms:")
        list = lines[i*4+x:i*4+4+x]
        shuffle(list)

        for line in list:
            print("  - " + line.strip())

    x += 8

if len(lines) > x:
    for i in range(2):
        print("- Exercise: easy")
        print("  Terms:")
        print("  - " + lines[i * 2 + x].strip())
        print("  - " + lines[i * 2 + 1 + x].strip())

        # Exercise: four_one x 2
    for i in range(1):
        print("- Exercise: four_one")
        print("  Terms:")
        list = lines[i * 4 + x:i * 4 + 4 + x]
        shuffle(list)

        for line in list:
            print("  - " + line.strip())

        # Exercise: identify_image x 2
    for i in range(1):
        print("- Exercise: identify_image")
        print("  Terms:")
        list = lines[i * 4 + x:i * 4 + 4 + x]
        shuffle(list)

        for line in list:
            print("  - " + line.strip())
