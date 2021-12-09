# https://codeup.kr/problem.php?id=1441
# 1441: 버블 정렬

num = int(input())
num_list = [int(input()) for _ in range(num)]

for i in range(len(num_list)-1,0,-1):
    for j in range(i):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

for item in num_list:
    print(item)