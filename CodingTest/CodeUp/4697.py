n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
map2 = map[:]
area = []

def dfs(x,y,max_num):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    
    global count
    if map[x][y] > max_num:
        map[x][y] = -1
        dfs(x+1,y,max_num)
        dfs(x-1,y,max_num)
        dfs(x,y+1,max_num)
        dfs(x,y-1,max_num)
        count += 1
        return True
    return False

max_num = max(max(map))

length = []
count = 0
for k in range(max_num,0,-1):
    area = []
    for i in range(n):
        for j in range(n):
            count = 0
            if map[i][j] > k:
                dfs(i,j,k)
                area.append(count)
        map = map2[:]
    print(k, area)
    length.append(len(area))
print(length)