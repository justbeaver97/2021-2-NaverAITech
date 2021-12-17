# https://www.acmicpc.net/problem/2667
# 2667번: 단지 번호 붙이기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = []
for _ in range(n):
    tmp = list(map(int, input()))
    graph.append(tmp)

def dfs(x,y):
    global size
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<n) and (0<=ny<n):
            if graph[nx][ny] > 0:
                graph[nx][ny] = -1
                size += 1
                dfs(nx, ny)
    
numApart, size = 0, 0
totalSize = []
for i in range(n):
    for j in range(n):
        size = 0
        if graph[i][j] > 0:
            dfs(i,j)
            numApart += 1
            if size == 0: 
                totalSize.append(1)
            else:
                totalSize.append(size)
        
            
print(numApart)
for item in sorted(totalSize):
    print(item)            