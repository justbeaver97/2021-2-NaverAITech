# https://www.acmicpc.net/problem/1676
# 1676번: 팩토리얼 0의 개수

n = int(input())

fact = 1
for i in range(1,n+1):
    fact *= i

toList = list(str(fact))
for i in range(len(toList)-1,-1,-1):
    if toList[i] != '0':
        if i == 0:
            print(0)
        else:
            print(len(toList)-i-1)
        break