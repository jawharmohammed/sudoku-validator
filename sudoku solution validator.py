import copy
def valid_solution(board):
    s=[]
    l=copy.deepcopy(board)
    for i in range(9):
        for j in range(9):
            l[i][j]=board[j][i]
    for i in range(9):
        for j in range(9):
            if board[i].count(board[i][j])!=1 or l[i].count(l[i][j])!=1 or board[i][j]==0:
                return False
    for i in range(0,7,3):
        for j in range(0,7,3):
            s=board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
            for k in range(9):
                if s.count(s[k])!=1:
                    return False
    return True

