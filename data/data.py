import sys

file_path = sys.argv[1]

i = 0

tok = []
lab = []

for line in open(file_path):
    if (i) % 3 == 0:
        ls = line.strip().split(" ")
        ls.append(' ')
        tok.extend(ls)
        # print(i + 1, ls)
    elif (i - 1) % 3 == 0:
        ls = line.strip().split(" ")
        ls.append(' ')
        lab.extend(ls)
        # print(i + 1, ls)
    i = i + 1

for i in range(len(tok)):
    print(tok[i], lab[i])