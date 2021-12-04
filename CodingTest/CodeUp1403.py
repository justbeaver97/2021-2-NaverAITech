# https://codeup.kr/problem.php?id=1403
# 1403: 배열 두번 출력하기

k = int(input())
input_arr = []

input_arr = input().split()

for j in range(2):
    for i in range(k):
        print(input_arr[i])