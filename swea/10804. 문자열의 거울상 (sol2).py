T = int(input())
for test_case in range(1, T + 1):
    s = input()
    s = s[::-1]
    ans = ""
    for i in s:
        if i == "b":
            ans += "d"
        elif i == "d":
            ans += "b"
        elif i == "p":
            ans += "q"
        elif i == "q":
            ans += "p"
    print("#" + str(test_case) + " " + ans)
