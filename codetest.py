from sys import exit
from random import shuffle
import random


file = open("example.txt", "r")
lines = file.readlines()
file.close()

while len(lines) % 4 != 0:
    lent = len(lines)
    num1 = random.randint(0, lent)
    new_list = new_list.append(lines[num1])
    lines.append(new_list)

fid = open("example.txt", "w")
fid.writelines(lines)
fid.close()


it = 0
iter = len(lines) // 8
x = 0
k = 0

rng = 0
rng2 = 0

print(iter)

for it in range(iter):
    if len(lines) - x == 4:
        rng = 2
        rng2 = 1
    else:
        rng = 4
        rng2 = 2
    # Exercise: easy x 4
    for i in range(rng):
        print("- exercise: easy")
        print("  terms:")
        print("  - " + lines[i * 2 + x].strip())
        print("  - " + lines[i * 2 + 1 + x].strip())

    # Exercise: four_one x 2
    for i in range(rng2):
        print("- exercise: four_one")
        print("  terms:")
        list = lines[i * 4 + x:i * 4 + 4 + x]
        shuffle(list)
        for line in list:
            print("  - " + line.strip())
    # Exercise: identify_image x 2

    for i in range(rng2):
        print("- exercise: identify_image")
        print("  terms:")
        list = lines[i * 4 + x:i * 4 + 4 + x]
        shuffle(list)
        for line in list:
            print("  - " + line.strip())
    x += 8

for k in range(len(lines)):
    print("- exercise: spell_term")
    print("  terms:")
    list = lines[k:k+1]
    for line in list:
        print("  - " + line.strip())
