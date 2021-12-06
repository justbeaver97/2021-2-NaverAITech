# https://codeup.kr/problem.php?id=1990
# 1990: 3의 배수 판별하기

n = input()
sum = 0

for i in range(len(n)):
    sum += int(n[i])

if sum % 3 == 0:
    print("1")
else:
    print("0")