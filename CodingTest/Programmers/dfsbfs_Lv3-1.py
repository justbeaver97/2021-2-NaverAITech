def make_list(n):
    return [0] * (n)

def dfs(v, visit_list, computers, n):
    visit_list[v] = 1
    for i in range(0, n):
        if visit_list[i]==0 and computers[v][i]==1:
            dfs(i, visit_list, computers, n)
    return visit_list
        
def solution(n, computers):
    answer = 0
    
    visit_list = make_list(n)
    tmp_list = visit_list[:]
    for i in range(0, n):
        visit_list = dfs(i, visit_list, computers, n) 
        if visit_list == tmp_list:
            continue
        else:
            tmp_list = visit_list[:]
            answer += 1
        
    return answer