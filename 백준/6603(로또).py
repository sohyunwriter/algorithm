import sys
input = sys.stdin.readline
def solve(nums):
    results = []

    def dfs(nums, pos, sublist=[]):
        if sublist and len(sublist) == 6:
            results.append(sublist[:])

        for i in range(pos+1, len(nums)):
            dfs(nums, i, sublist + [nums[i]])

    dfs(nums, -1, [])
    return results

if __name__ == "__main__":
    while True:
        k, *S = map(int, input().split())
        if k == 0:
            break

        ans = solve(S)

        for i in ans:
            print(*i)
        print()
