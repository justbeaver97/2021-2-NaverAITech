# https://www.acmicpc.net/problem/1929
# 1929번: 소수 구하기

m, n = map(int, input().split())
primeNum = []
if n>2:
    for i in range(m,n+1):
        if i==1:
            continue
        if i==2:
            primeNum.append(2)
            continue
        for j in range(2,n-1):
            if i%j==0:
                break
            if j >= i-1 and i%j != 0:
                primeNum.append(i)
elif n==2:
    primeNum.append(2)
# for item in primeNum:
#     print(item)
print(len(primeNum))