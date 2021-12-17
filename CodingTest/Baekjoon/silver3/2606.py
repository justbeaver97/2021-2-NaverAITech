# https://www.acmicpc.net/problem/2606
# 2606번: 바이러스

def dfs(v):
    global count
    visit_list[v] = 1
    for i in range(1, comNum+1):
        if visit_list[i] == 0 and link[v][i] == 1:
            dfs(i)
            count += 1
             
comNum = int(input())
comLink = int(input())
visit_list = [0] * (comNum+1)
link = [[0]*(comNum+1) for _ in range(comNum+1)]
count = 0
for _ in range(comLink):
    a,b = map(int, input().split())
    link[a][b] = link[b][a] = 1
dfs(1)
print(count)