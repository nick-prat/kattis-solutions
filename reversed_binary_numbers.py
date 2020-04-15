import sys
import math

N = int(sys.stdin.readline().strip())

Q = N
ans = 0

for i in reversed(range(math.ceil(math.log(N+1, 2)))):
    ans = int(ans + Q%2 * math.pow(2,i))
    Q = math.floor(Q/2)
    if Q == 0:
        break

print(ans)

