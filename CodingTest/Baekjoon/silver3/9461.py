# https://www.acmicpc.net/problem/9461
# 9461번: 파도반 수열

t = int(input())
n = []
for _ in range(t):
    tmp = int(input())
    n.append(tmp)
    
padovan = [1,1,1,2,2]
for i in range(4,max(n)-1):
    tmp = padovan[i] + padovan[i-4]
    padovan.append(tmp)

for i in range(len(n)):
    print(padovan[n[i]-1])
