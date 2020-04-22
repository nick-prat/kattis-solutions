import math, sys

def is_vowel(char):
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y'

def count(word):
    D = 0

    for i in range(len(word) - 1):
        if word[i] == word[i+1] and is_vowel(word[i]):
            D += 1
    
    return D

while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break
    
    words = [sys.stdin.readline().strip() for n in range(N)]
    favorite = words[0]
    M = 0
    for i in range(N):
        D = count(words[i])
        if D > M:
            M = D
            favorite = words[i]
    print(favorite)
