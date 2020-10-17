T = int(input())
for test_case in range(1, T + 1):
    s = input()
    sl = []
    for i in s:
        if i == "b":
            sl.append("d")
        elif i == "d":
            sl.append("b")
        elif i == "p":
            sl.append("q")
        elif i == "q":
            sl.append("p")

    ans = ""
    while len(sl) > 0:
        ans += sl.pop()
    print("#" + str(test_case) + " " + ans)
