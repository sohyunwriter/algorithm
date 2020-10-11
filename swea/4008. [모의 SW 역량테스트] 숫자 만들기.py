def permute(sum, opers, opersNum):
    results = []

    def dfs(sum, opers, opersNum):
        if opersNum == 0:
            results.append(sum[:])
            return

        for i in range(4):
            if opers[i] > 0:
                opers[i] -= 1
                dfs(sum+str(i), opers, opersNum-1)
                opers[i] += 1

    dfs(sum, opers, opersNum)
    return results

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    popers = permute("",  opers, N-1)
    results = []
    for poper in popers:
        temp = 0
        for i, v in enumerate(poper):
            if i == 0:
                temp = nums[i]

            if v == "0":
                temp += nums[i+1]
            elif v == "1":
                temp -= nums[i+1]
            elif v == "2":
                temp *= nums[i+1]
            elif v == "3":
                temp = int(temp/nums[i+1])

        results.append(temp)

    ans = max(results) - min(results)
    print("#" + str(test_case) + " " + str(ans))
