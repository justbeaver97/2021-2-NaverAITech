def mergeSort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    front_arr = mergeSort(arr[mid:])
    back_arr = mergeSort(arr[:mid])
    
    merged_arr = []
    h, l = 0, 0
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

print(mergeSort([6,1,2,3,9,4,1]))