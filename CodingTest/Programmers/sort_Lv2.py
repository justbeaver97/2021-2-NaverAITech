# def toString(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = str(numbers[i])
#     return numbers

# def sort(array):
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i]>array[j]:
#                 tmp = array[i]
#                 array[i] = array[j]
#                 array[j] = tmp
#     return array

# def sortArray(stringArr):
#     for i in range(len(stringArr)):
#         for j in range(len(stringArr)):
#             if stringArr[i][0]>stringArr[j][0]:
#                 tmp = stringArr[i]
#                 stringArr[i] = stringArr[j]
#                 stringArr[j] = tmp
#     return stringArr

# def solution(numbers):
#     answer = ''
#     sortArr = []
#     stringArr = []
#     bigArr = []
    
#     sortArr = sort(numbers)
#     stringArr = toString(sortArr)
#     print(stringArr)
#     bigArr = sortArray(stringArr)
#     print(bigArr)
    
#     for item in bigArr:
#         answer += item
    
#     return answer

# print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))

        