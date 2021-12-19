# https://www.acmicpc.net/problem/11653
# 11635번: 소인수분해

n = int(input())

i, start = 2, n
num = []
for _ in range(n):
    if start % i == 0:
        start = int(start / i)
        num.append(i)
        i = 2
    else:
        i += 1
    if start == 1:
        break

for item in num:
    print(item)