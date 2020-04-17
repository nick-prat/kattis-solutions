import sys, math

move_set = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
move_limit = 10

def board_string(board):
    new = "" 
  
    for row in board:
        for char in row:
            new += char
  
    return new 

def print_board(board):
    for row in board:
        print(row)

def find_empty(board):
    for r in range(5):
        for c in range(5):
            if board[r][c] == ' ':
                return r,c
    return -1,-1

def swap(board, r, c, nr, nc):
    temp = board[r][c]
    board[r][c] = board[nr][nc]
    board[nr][nc] = temp
    return board

def check_bound(r, c):
    return r < 5 and r >= 0 and c < 5 and c >= 0

def copy_board(board):
    nboard = []
    for row in board:
        nboard.append(row.copy())
    return nboard

def splitstr(line):
    return [char for char in line]

def check_board(board):
    for r in range(2):
        for c in range(r, 5):
            if board[r][c] != '1':
                return False

    if board[2][2] != ' ':
        return False

    for r in range(2, 4):
        for c in range(r+1, 5):
            if board[r][c] != '1':
                return False
    
    return True

def num_wrong(board):
    w = 0
    for r in range(2):
        for c in range(r, 5):
            if board[r][c] == '0':
                w += 1

    for r in range(2, 4):
        for c in range(r+1, 5):
            if board[r][c] == '0':
                w += 1

    return w

def dfs(board, pr, pc, er, ec, move_count, move_lim):
    if check_board(board):
        return move_count
    
    if move_count + num_wrong(board) >= move_lim:
        return -1

    ans = []
    for offr, offc in move_set:
        tr = er + offr
        tc = ec + offc
        if pr == tr and pc == tc:
            continue

        if(check_bound(tr, tc)):
            swap(board, er, ec, tr, tc)
            res = dfs(board, er, ec, tr, tc, move_count + 1, move_lim)
            if res != -1:
                ans.append(res)
            swap(board, er, ec, tr, tc)
    
    if len(ans) > 0:
        return min(ans)
    return -1

N = int(sys.stdin.readline().strip())

for n in range(N):
    board = [splitstr(sys.stdin.readline().strip('\n')) for i in range(5)]
    
    r, c = find_empty(board)
    ans = dfs(board, r, c, r, c, 0, move_limit)

    if ans != -1:
        print("Solvable in {} move(s).".format(ans))
    else:
        print("Unsolvable in less than {} move(s).".format(move_limit + 1))
