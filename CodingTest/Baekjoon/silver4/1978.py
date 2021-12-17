# https://www.acmicpc.net/problem/1978
# 1978번: 소수 찾기

n = int(input())
num = list(map(int, input().split()))

primeNum = []
for i in range(n):
    if num[i] == 2:
        primeNum.append(num[i])
    if num[i] > 2:    
        for j in range(2,num[i]):
            if num[i] % j == 0:
                break
            if j == num[i]-1 and num[i]%j != 0:
                primeNum.append(num[i])
    else:
        continue
# print(primeNum)
print(len(primeNum))