import math, sys

def splitstr(line):
    return [char for char in line]

def swap(word, i, C):
    temp = word[C]
    word[C] = word[i]
    word[i] = temp

def is_palindrome(str):
    L = len(str)
    for i in range(math.ceil(L/2)):
        if str[i] != str[L-1-i]:
            return False
    return True

N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for n in range(N)]

for word in words:
    if is_palindrome(word):
        print(0)
        continue

    chars = splitstr(word)
    L = len(chars)
    A = 0
    for i in range(math.floor(L/2)):
        C = L-i-1
        B = i

        if chars[B] == chars[C]:
            continue

        S, D = -1, -1
        for j in range(1, C-B):
            if chars[B] == chars[C-j]:
                S = C-j
                D = C
                break
            if chars[C] == chars[B+j]:
                S = B+j
                D = B
                break
        
        if S == -1:
            A = 0
            break

        K = -1 if D < S else 1
        for j in range(S, D, K):
            if chars[j] == chars[j+K]:
                continue
            A += 1
            swap(chars, j, j + K)
    
    if A == 0:
        print("impossible")
    else:
        print(A)