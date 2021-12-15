# https://www.acmicpc.net/problem/1157
# 1157번: 단어 공부

word = list(map(str, input()))

letter = []
for i in range(65,91):
    letter.append(0)
            
for i in range(len(word)):
    if ord(word[i]) < 91:
        letter[ord(word[i])-65] += 1
    else:
        letter[ord(word[i])-32-65] += 1
   
largest = max(letter)
match, index = 0, 0

for i in range(len(letter)):
    if letter[i] == largest:
        match += 1
        index = i

if match == 1:
    print(chr(index+65))
else:
    print("?")