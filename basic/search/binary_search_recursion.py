def binary_search_recursion(data, start, end, target):
    if start > end:
        return -1

    mid = (start+end) // 2

    if data[mid] == target:
        return mid
    else:
        if data[mid] > target:
            return binary_search_recursion(data, start, mid-1, target)
        else:
            return binary_search_recursion(data, mid+1, end, target)
            

# this is for test
if __name__ == "__main__":
    data_list = []
    print("array 입력 (예) 1 2 3 4 5: ")
    s = input()
    for item in s.split(" "):
        data_list.append(int(item))

    data_list.sort()
    print(data_list)
    print("찾고자 하는 값 입력 : ")

    target = int(input())
    ans = binary_search_recursion(data_list, 0, len(data_list)-1, target)
    print("찾고자 하는 값 : %d 찾고자 하는 값의 위치 : %d" %(target, ans))
