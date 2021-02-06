def solution(n, arr1, arr2):
    answer = []
    for i in range(0, n):
        s = "{0:b}".format(arr1[i] | arr2[i]).zfill(n)
        s = s.replace("1", "#")
        s = s.replace("0", " ")
        answer.append(s)
    return answer
