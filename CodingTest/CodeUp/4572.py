# https://codeup.kr/problem.php?id=4572
# 4572: 영역 구하기

m, n, k = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(k)]
graph = [[0]*m for i in range(n)]
area = []

def fill_in(x1,y1,x2,y2, graph):
    for i in range(x1,x2,1):
        for j in range(y1,y2,1):
            graph[i][j] = 1
    return graph

for i in range(k):
    graph = fill_in(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],graph)
print(graph)

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    global count

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        count += 1
        return True
    return False

for i in range(n):
    for j in range(m):
        count = 0
        if graph[i][j] == 0:
            dfs(i,j)
            area.append(count)

print(graph)

print(len(area))
sorted_area = sorted(area)
for i in range(len(sorted_area)):
    if i == len(sorted_area)-1:
        print(sorted_area[i])
    else:
        print(sorted_area[i],end=' ')