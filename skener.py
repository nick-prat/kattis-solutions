import sys

def splitStr(str):
    return [char for char in str]

IN = sys.stdin.readline().strip()
R, C, Zr, Zc = map(int, IN.split(" "))

mat = []
for i in range(R):
    mat.append(splitStr(sys.stdin.readline().strip()))

for i in range(R):
    for iz in range(Zr):
        for j in range(C):
            for jz in range(Zc):
                print(mat[i][j], end = '')
        print("")

