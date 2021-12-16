# https://www.acmicpc.net/problem/11650
# 11650번: 좌표 정렬하기

n = int(input())

xy = []
for i in range(n):
    tmp = list(map(int, input().split()))
    xy.append(tmp)
    
xy = sorted(xy, key = lambda x: (x[0], x[1]))
for i in range(len(xy)):
    print(xy[i][0],xy[i][1])