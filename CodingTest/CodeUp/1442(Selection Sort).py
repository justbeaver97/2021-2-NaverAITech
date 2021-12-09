# https://codeup.kr/problem.php?id=1442
# 1442: 선택 정렬

num = int(input())
num_list = [int(input()) for _ in range(num)]

for i in range(len(num_list)-1, 0, -1):
    index = i
    for j in range(i):
        if num_list[index] < num_list[j]:
            index = j
    num_list[i], num_list[index] = num_list[index], num_list[i]

for item in num_list:
    print(item)