f = open("output.txt", "r")
lines = f.read().splitlines() # 개행문자를 제거하기 위해 splitlines() 사용
f.close()

for test_case in range(1, T + 1): 
    # 문제풀이코드~~~~

    # 각 행마다 출력하는 값이 정답인지 확인하기
    if lines[test_case-1] == "#" + str(test_case) + " " + str(answer):
        print("true")
    else:
        print("false")
