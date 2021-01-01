def solution(A):
    array = [True for _ in range(1000001)]
    
    for i in A:
        if i > 0 and array[i]:
            array[i] = False
    
    for i in range(1, len(array)):
        if array[i]:
            return i
