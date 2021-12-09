# https://codeup.kr/problem.php?id=1420
# 1420: 3등 찾기

num = int(input())

list = []
for i in range(num):
    tmp = []
    name, score = input().split()
    tmp.append(name)
    tmp.append(int(score))
    list.append(tmp)

sorted_list = sorted(list, key = lambda x: x[1], reverse=True)
print(sorted_list[2][0])
