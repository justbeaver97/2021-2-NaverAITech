def solution(n, lost, reserve):
    answer = 0
    
    tmpLost, tmpReserve = lost[:], reserve[:]
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == 1:
                if lost[i] == reserve[j]-1 or lost[i] == reserve[j]:
                    if lost[i] in tmpLost and reserve[j] in tmpReserve:
                        tmpLost.remove(lost[i])
                        tmpReserve.remove(reserve[j])
            elif 1 < lost[i] < n:
                if lost[i] == reserve[j]+1 or lost[i] == reserve[j] or lost[i] == reserve[j]-1:
                    if lost[i] in tmpLost and reserve[j] in tmpReserve:
                        tmpLost.remove(lost[i])
                        tmpReserve.remove(reserve[j])
            else:
                if lost[i] == reserve[j] or lost[i] == reserve[j]+1:
                    if lost[i] in tmpLost and reserve[j] in tmpReserve:
                        tmpLost.remove(lost[i])
                        tmpReserve.remove(reserve[j])
                
    answer = n - len(tmpLost)
    
    return answer