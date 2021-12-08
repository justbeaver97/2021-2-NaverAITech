# 버블정렬: O(N^2)
# 선택정렬: O(N^2)
# 퀵정렬: O(N^2)
# 삽입정렬: O(N^2)
# 힙정렬: O(NlogN)
# 병합정렬: O(NlogN)
# 기수정렬: O(N)
# 카운팅정렬: O(N)

# https://devjin-blog.com/sort-algorithm-9/

class RadixSort:
    def __init__(self, num):
        self.num = num

    def radix_sort(self):
        # 최대 digit을 알아보기 위해 가장 큰 수를 찾는다
        max1 = max(self.num) 
    
        exp = 1
        while max1/exp > 0: 
            self.count_sort(self.num,exp) 
            exp *= 10


    def count_sort(self, A, k):
        B = [0] * len(A)
        C = [0] * (10) # 1의 자리, 10의 자리수만 비교하기 때문에 범위는 0~9이다

        for i in range(0, len(A)): # 각 element가 몇개있는지 C에 저장한다
            index = (A[i]//k) 
            C[ (index)%10 ] += 1
        
        for i in range(1,10): # C를 누적값으로 바꾼다, 0~9까지 밖에 없다
            C[i] += C[i-1]

        i = len(A)-1
        while i>=0:  # C 를 indexing해서 정렬된 리스트를 찾는다
            index = (A[i]//k) 
            B[ C[ (index)%10 ] - 1] = A[i] 
            C[ (index)%10 ] -= 1
            i -= 1

        # 기존 리스트에 복사를 한다
        for i in range(len(A)): 
            A[i] = B[i]

number = [ 170, 45, 75, 90, 802, 24, 2, 66] 
print(number)
radix = RadixSort(number)
radix.radix_sort() 
print(radix.num)