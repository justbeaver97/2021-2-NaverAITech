# https://www.acmicpc.net/problem/2751
# 2751번: 수 정렬하기2

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    frontArr = mergeSort(arr[mid:])
    backArr = mergeSort(arr[:mid])
    
    mergedArr = []
    l, h = 0, 0
    while l < len(frontArr) and h < len(backArr):
        if frontArr[l] < backArr[h]:
            mergedArr.append(frontArr[l])
            l += 1
        else:
            mergedArr.append(backArr[h])
            h += 1
    mergedArr += frontArr[l:]
    mergedArr += backArr[h:]
    return mergedArr

n = int(input())

number = []
for i in range(n):
    tmp = int(input())
    number.append(tmp)

print(mergeSort(number))