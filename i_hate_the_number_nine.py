import sys, math

def exponent_mod(base, exp, mod):
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod

    index = 0
    exps = []
    while exp > 0:
        if exp % 2 == 1:
            exps.append(2**index % mod)
        exp = exp >> 1
        index = index + 1

    ans = 1
    for exp in exps:
        print("ans: {} base: {} exp: {}".format(ans, base, exp))
        ans = (ans * (base ** exp) % mod) % mod
    return ans

N = int(sys.stdin.readline().strip())
cases = [int(sys.stdin.readline().strip()) for i in range(N)]

mod = 1000000007
for case in cases:
    print(8 * exponent_mod(9, case - 1, mod) % mod)