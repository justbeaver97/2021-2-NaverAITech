# https://www.acmicpc.net/problem/2609
# 2609번: 최대공약수와 최소공배수

m, n = map(int, input().split())

yak = 1
if m > n:
    for i in range(1,m+1):
        if n % i == 0 and m % i == 0:
            yak = i
else:
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            yak = i
a = int(m / yak)
b = int(n / yak)
print(yak)
print(yak*a*b)