# https://codeup.kr/problem.php?id=3004
# 3004: 데이터 재정렬

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    front_arr = merge_sort(arr[mid:])
    back_arr = merge_sort(arr[:mid])
    
    merged_sort = []
    l, h = 0, 0
    
    while l < len(front_arr) and h < len(back_arr):
        if front_arr[l] < back_arr[h]:
            merged_sort.append(front_arr[l])
            l += 1
        else:
            merged_sort.append(back_arr[h])
            h += 1
    merged_sort += front_arr[l:]
    merged_sort += back_arr[h:]
    return merged_sort

def re_sort(array, sorted_list):
    index = []
    num = 0
    for item in sorted_list:
        count = 0
        tmp = []
        for item2 in array:
            if item == item2:
                tmp.append(count)
                tmp.append(num)
                index.append(tmp)
            count += 1
        num += 1
    return index
        

n = int(input())
array = list(map(int, input().split()))
sorted_list = merge_sort(array)

# num_list = []
# for i in range(len(sorted_list)):
#     num_list.append(i)
    
# zipped_list = list(zip(sorted_list, num_list))


# zipped_list = list(zip(array, sorted_list, num_list))
# print(zipped_list)
# final_list = sorted(zipped_list, key=lambda x:x[0])
# print(final_list)

# abc = []
# for item in array:
#     if item in sorted_list:
#         abc.append(sorted_list[item])




resort_list = re_sort(array, sorted_list)
resort_list.sort()

for i in range(len(resort_list)):
    if i == len(resort_list)-1:
        print(resort_list[i][1])
    else:
        print(resort_list[i][1], end=' ')