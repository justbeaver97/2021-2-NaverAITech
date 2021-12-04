# https://codeup.kr/problem.php?id=1368
# 1368: 평행사변형 출력하기2

h, k, d = input().split()

if d == "L":
    for i in range(int(h)):
        print(" "*i,end="")
        for j in range(int(k)):
            print("*",end="")
        print()
        
else:
    for i in range(int(h)):
        print(" "*(int(h)-i-1), end="")
        for j in range(int(k)):
            print("*",end="")
        print()