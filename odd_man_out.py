import sys

N = int(sys.stdin.readline().strip())

for i in range(int(N)):
    G = int(sys.stdin.readline().strip())
    tokens = sys.stdin.readline().split()
    for case in range(G):
        if tokens.count(tokens[case]) == 1:
            print("Case #{}: {}".format(i + 1, tokens[case]))
            break