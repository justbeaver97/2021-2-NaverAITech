# https://codeup.kr/problem.php?id=1754
# 1754: 큰 수 비교

n1, n2 = list(input().split())

if len(n1)>len(n2):
    print(n2, n1)
elif len(n1)<len(n2):
    print(n1, n2)
else:
    for i in range(len(n1)):
        if n1[i] == n2[i]:
            continue
        elif n1[i] > n2[i]:
            print(n2, n1)
            break
        else:
            print(n1, n2)
            break