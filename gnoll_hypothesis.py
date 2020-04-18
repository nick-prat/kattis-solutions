import math, sys

N, K = [int(v) for v in sys.stdin.readline().strip('\n').split(" ")]
S = [float(s) for s in sys.stdin.readline().strip('\n').split(" ")]

# ! Tied for fastest python3 solution on kattis as of 04/18/2020 01:32 AM, 0.07s

if K == 0:
    for I in range(N):
        print("0.0", end = ' ')
else:
    D = N - K
    Q = K / N
    for I in range(N):
        R = Q
        P = R * S[I]
        for J in range(1, D + 1):
            R *= ((D - J + 1) / (N - J))
            P += R * S[(I - J) % N]
        print(P, end = ' ')
print()