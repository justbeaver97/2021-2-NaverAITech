# https://codeup.kr/problem.php?id=1172
# 1172: 세 수 정렬하기

input_list = list(map(int, input().split()))

for i in range(len(input_list)):
    for j in range(len(input_list)-1):
        if input_list[j] > input_list[j+1]:
            tmp = input_list[j]
            input_list[j] = input_list[j+1]
            input_list[j+1] = tmp
    
for i in range(len(input_list)):
    if i == len(input_list)-1:
        print(input_list[i])
    else:
        print(input_list[i], end=' ')