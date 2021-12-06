# https://codeup.kr/problem.php?id=1501
# 1501: 2차원 배열 채우기1

n = int(input())
num = 1

for i in range(n):
    for j in range(n):
        print(num, end=" ")
        num += 1
    print()