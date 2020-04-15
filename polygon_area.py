import sys
import math

def det(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break

    coords = []
    for i in range(N):
        coords.append(list(map(int, sys.stdin.readline().split(" "))))
    
    mats = []
    for i in range(len(coords)):
        mats.append([ [coords[i][0],coords[(i + 1) % len(coords)][0]], [coords[i][1], coords[(i + 1) % len(coords)][1]] ])
    
    ans = sum(list(map(det, mats))) * 0.5
    print("{} {}".format("CW" if ans < 0 else "CCW", abs(ans)))