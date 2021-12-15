# https://www.acmicpc.net/problem/4673
# 4673번: 셀프 넘버

num = []
for i in range(1,10000):
    num.append(i)

for i in range(len(num)):
    if i >= 1000:
        tmp = i + i // 1000 + i // 100 % 10 + i // 10 % 10 + i % 10
        if tmp in num:
            num.remove(tmp)
    elif i >= 100:
        tmp = i + i // 100 + i // 10 % 10 + i % 100 % 10
        if tmp in num:
            num.remove(tmp)
    elif i >= 10:
        tmp = i + i // 10 + i % 10
        if tmp in num:
            num.remove(tmp)
    else:
        tmp = i + i
        if tmp in num:
            num.remove(tmp)
        
    
for item in num:
    print(item)