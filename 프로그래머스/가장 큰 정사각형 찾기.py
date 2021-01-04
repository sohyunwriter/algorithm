def solution(board):
    max = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:  # 0이면 막힘
                continue
            
            if max == 0: # 1이 있으면 정사각형 최소 1 존재
                max = 1
                
            if i == 0 or j == 0: # i=0이거나 j=0일 때는 값 변동x
                continue
            
            board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1 # 정사각형 개수 업데이트
            
            if board[i][j] > max:
                max = board[i][j]
                
    answer = max ** 2
    
    return answer
