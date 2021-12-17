# https://www.acmicpc.net/problem/7576
# 7576번: 토마토

# 1과 -1만 그래프에 있으면 됨

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    for _ in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        

m, n = map(int, input().split())
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
print(graph)