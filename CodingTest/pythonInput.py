# 숫자 input 하나씩
input1, input2, input3 = map(int, input().split())
print("{} + {} + {} = {}".format(input1, input2, input3, input1 + input2 + input3))

# 숫자 input 배열로
input_list = list(map(int, input().split()))
for i in range(len(input_list)):
    print(input_list[i],end=' ')
print()

# 문자열 input 하나씩
word1, word2, word3 = input().split()
print("{} {} {}".format(word1, word2, word3))

# 문자열 input 배열로
word_list = [input() for _ in range(5)]
print(word_list)
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW

# 문자열 input 각 문자마다
word_list2 = [list(map(int, input())) for _ in range(4)]
print(word_list2)
# 101111
# 101010
# 101011
# 111011