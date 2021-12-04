# https://codeup.kr/problem.php?id=1407
# 1407: 문자열 출력하기1

inputArr = []
inputArr = input().split()

for i in range(len(inputArr)):
    if i == len(inputArr)-1:
        print(inputArr[i])
    else:
        print(inputArr[i],end="")