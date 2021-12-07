def sort(array):
    # print("기존",array)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]<array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
    # print("정렬",array)
    return array

def solution(array, commands):
    temp = []
    sliced = []
    answer = []
    
    for i in range(len(commands)):
        start = commands[i][0]-1
        end = commands[i][1]
        temp = array[start:end]
        sliced.append(sort(temp))
    # print(sliced)
    
    for i in range(len(sliced)):
        index = commands[i][2]-1
        answer.append(sliced[i][index])
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))