import math, sys

N, K = [int(v) for v in sys.stdin.readline().strip('\n').split(" ")]
S = [float(s) for s in sys.stdin.readline().strip('\n').split(" ")]

# ! Tied for fastest python3 solution on kattis as of 04/18/2020 01:32 AM, 0.07s
A = []
for I in range(N):
    if K == 0:
        A.append(float(0))
        continue

    P = 0
    R = 1
    for J in range(N - K + 1):
        if J == 0:
            R = R * (K / N)
        else:
            R = R * ((N - K - J + 1) / (N - J))
        P = P + R * S[(I - J) % N]
    A.append(P)

for a in A:
    print("{}".format(a), end=' ')
print()