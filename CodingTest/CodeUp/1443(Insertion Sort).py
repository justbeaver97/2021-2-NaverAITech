# https://codeup.kr/problem.php?id=1443
# 1443: 삽입 정렬

n = int(input())
list = [int(input()) for _ in range(n)]

for i in range(1,len(list)):
    for j in range(i, 0, -1):
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]

print(list)