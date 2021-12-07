# https://codeup.kr/problem.php?id=1378
# 1378: 수열의 합

n = int(input())
sum, total = 0, 0

for i in range(1,n+1):
    for j in range(1,i+1):
        sum += j
    total += sum
    sum = 0
print(total)