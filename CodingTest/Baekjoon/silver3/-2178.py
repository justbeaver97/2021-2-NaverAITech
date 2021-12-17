# https://www.acmicpc.net/problem/2178
# 2178번: 미로 탐색

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

def dfs(x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<n) and (0<=ny<m):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)
                cnt += 1

n, m = map(int, input().split())
graph = []

for _ in range(n):
    tmp = list(map(int, input()))
    graph.append(tmp)
    
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            dfs(i,j)

print(cnt)