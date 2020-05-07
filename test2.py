import random

fid = open("example.txt", "r")
li = fid.readlines()
fid.close()

i = 0
j = 0
lung = 0
long = 0

while lung < len(li):
    ls = li[lung:lung + 8]
    print("- exercise: easy")
    print("  terms:")
    print("  - " + ls[j])
    print("  - " + ls[j + 1])
    print("- exercise: easy")
    print("  terms:")
    print("  - " + ls[j + 2])
    print("  - " + ls[j + 3])
    print("- exercise: easy")
    print("  terms:")
    print("  - " + ls[j + 4])
    print("  - " + ls[j + 5])
    print("- exercise: easy")
    print("  terms:")
    print("  - " + ls[j + 6])
    print("  - " + ls[j + 7])
    ls1 = ls[i:i + 4]
    random.shuffle(ls1)
    ls2 = ls[i + 4:i + 8]
    random.shuffle(ls2)
    print("- exercise: four_one")
    print("  terms:")
    print("  - " + ls1[i])
    print("  - " + ls1[i + 1])
    print("  - " + ls1[i + 2])
    print("  - " + ls1[i + 3])
    print("- exercise: four_one")
    print("  terms:")
    print("  - " + ls2[i])
    print("  - " + ls2[i + 1])
    print("  - " + ls2[i + 2])
    print("  - " + ls2[i + 3])
    random.shuffle(ls1)
    random.shuffle(ls2)
    print("- exercise: identify_image")
    print("  terms:")
    print("  - " + ls1[i])
    print("  - " + ls1[i + 1])
    print("  - " + ls1[i + 2])
    print("  - " + ls1[i + 3])
    print("- exercise: identify_image")
    print("  terms:")
    print("  - " + ls2[i])
    print("  - " + ls2[i + 1])
    print("  - " + ls2[i + 2])
    print("  - " + ls2[i + 3])
    # li[i:i + 4] = ls1
    # li[i + 4:i + 8] = ls2
    lung += 8
    long = lung
    if len(li) - long == 4:
        short = li[lung:lung + 4]
        print("- exercise: easy")
        print("  terms:")
        print("  - " + short[j])
        print("  - " + short[j + 1])
        print("- exercise: easy")
        print("  terms:")
        print("  - " + short[j + 2])
        print("  - " + short[j + 3])
        random.shuffle(short)
        print("- exercise: four_one")
        print("  terms:")
        print("  - " + short[i])
        print("  - " + short[i + 1])
        print("  - " + short[i + 2])
        print("  - " + short[i + 3])
        random.shuffle(short)
        print("- exercise: identify_image")
        print("  terms:")
        print("  - " + short[i])
        print("  - " + short[i + 1])
        print("  - " + short[i + 2])
        print("  - " + short[i + 3])
        break


k = 0
while k < len(li):
    print("- exercise: spell_term")
    print("  terms:")
    print("  - " + li[k])
    k += 1

#fid = open("shuffled_example.txt", "w")
#fid.writelines(li)
#fid.close()