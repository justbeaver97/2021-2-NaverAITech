# https://www.acmicpc.net/problem/1316
# 1316번: 그룹 단어 체커

n = int(input())

word = []
for i in range(n):
    tmp = list(map(str, input()))
    word.append(tmp)

count, t = 0, 0
for i in range(len(word)):
    alphabet = []
    for j in range(1,len(word[i])):
        # print(alphabet, word[i][j-1],word[i][j])
        if alphabet == []:
            alphabet.append(word[i][0])
        if word[i][j] != word[i][j-1] and word[i][j] in alphabet:
            t = 1
            break
        alphabet.append(word[i][j])
    # print("check",t)
    if t == 1:
        t = 0
    else: 
        count += 1
print(count)