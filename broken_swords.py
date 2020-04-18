import math, sys

def splitstr(string):
    return [char for char in string]

swords = [splitstr(sys.stdin.readline().strip()) for i in range(int(sys.stdin.readline().strip()))]

tb = 0
lr = 0
for r in swords:
    for c in range(2):
        if r[c] == '0':
            tb += 1
    for c in range(2,4):
        if r[c] == '0':
            lr += 1

C = int(min(lr, tb) / 2)
print("{} {} {}".format(C, tb - C * 2, lr - C * 2))