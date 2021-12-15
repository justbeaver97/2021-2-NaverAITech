# https://www.acmicpc.net/problem/2751
# 2751번: 수 정렬하기2
# 시간 초과

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    frontArr = mergeSort(arr[mid:])
    backArr = mergeSort(arr[:mid])
    
    mergedSort = []
    l, h = 0, 0
    while l < len(frontArr) and h < len(backArr):
        if frontArr[l] < backArr[h]:
            mergedSort.append(frontArr[l])
            l += 1
        else:
            mergedSort.append(backArr[h])
            h += 1
    mergedSort += frontArr[l:]
    mergedSort += backArr[h:]
    return mergedSort

n = int(input())

number = []
for i in range(n):
    tmp = int(input())
    number.append(tmp)
    
sorted = mergeSort(number)
for item in sorted:
    print(item)