# https://codeup.kr/problem.php?id=1452
# 1452: 데이터 정렬(large)

def merge_sort(arr):
    if len(arr)<2:
        return arr
    
    mid = len(arr)//2
    front_arr = merge_sort(arr[mid:])
    back_arr = merge_sort(arr[:mid])
    
    merged_arr = []
    l, h = 0, 0
    while l < len(front_arr) and h < len(back_arr):
        if front_arr[l] < back_arr[h]:
            merged_arr.append(front_arr[l])
            l += 1
        else:
            merged_arr.append(back_arr[h])
            h += 1
    merged_arr += front_arr[l:]
    merged_arr += back_arr[h:]
    return merged_arr

n = int(input())
list = [int(input()) for _ in range(n)]

sorted_list = merge_sort(list)
for item in sorted_list:
    print(item)