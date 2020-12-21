def bubblesort(A):  # 버블소트 original
    for i in range(1, len(A)):
        for j in range(0, len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

N = int(input())
nums = [int(input()) for _ in range(N)]
nums_sorted = bubblesort(nums)
for i in nums_sorted:
    print(i)
