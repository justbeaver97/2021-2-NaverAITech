# https://www.acmicpc.net/problem/1259
# 1259번: 팰린드롬수

# while True:
#     num = list(map(int,input()))
#     if num == [0]:
#         break
#     if  num[:len(num)//2] == list(reversed(num[-(len(num)//2):])):
#         print("yes")
#     else:
#         print("no")

while True:
    num = input()
    if num == '0':
        break
    if  num == num[::-1]:
        print("yes")
    else:
        print("no")