import math, sys

N, P = map(int, sys.stdin.readline().strip().split(" "))
if N == 0:
    print(1)
    exit()

S = sum(map(int, sys.stdin.readline().strip().split(" ")))

if P == 100:
    print("impossible")
    exit()

print(math.ceil((S - P*N)/(P-100)))
