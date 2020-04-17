import sys, math

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
    for r in range(5):
        for c in range(0,r+1 if r > 2 else r):
            if board[r][c] != '0':
                return False

        for c in range(r+1 if r > 2 else r,5):
            if r == 2 and c == 2:
                if board[r][c] != ' ':
                    return False
                continue

            if board[r][c] != '1':
                return False
    return True

def dfs(board, pr, pc, move_count, move_limit):
    if check_board(board):
        return move_count
    
    if move_count >= move_limit:
        return -1

    ans = []
    r, c = find_empty(board)
    for offr in [-2,-1,1,2]:
        for offc in [-2,-1,1,2]:
            if abs(offr) == abs(offc):
                continue
            
            if pr == r + offr and pc == c + offc:
                continue

            if(check_bound(r + offr, c + offc)):
                swap(board, r, c, r + offr, c + offc)
                ans.append(dfs(board, r, c, move_count + 1, move_limit))
                swap(board, r, c, r + offr, c + offc)
    
    if len(ans) > 0:
        return min(ans)
    return -1

def bfs(oboard, move_limit):
    queue = []
    r, c = find_empty(oboard)
    queue.append([[r, c]])

    while(len(queue) > 0):
        board = copy_board(oboard)
        moves = queue.pop(0)

        pr, pc = 0, 0
        for move in moves:
            nr, nc = move
            pr, pc = find_empty(board)
            swap(board, pr, pc, nr, nc)

        if check_board(board):
            return len(moves) - 1

        if len(moves) >= move_limit + 1:
            continue
        
        r,c = find_empty(board)
        for offr in [-2,-1,1,2]:
            for offc in [-2,-1,1,2]:
                if abs(offr) == abs(offc):
                    continue
                
                if pr == r + offr and pc == c + offc:
                    continue

                if(check_bound(r + offr, c + offc)):
                    nmoves = moves.copy()
                    nmoves.append([r + offr, c + offc])
                    queue.append(nmoves)

    return -1

N = int(sys.stdin.readline().strip())

for n in range(N):
    limit = 5

    board = []
    for i in range(5):
        board.append(splitstr(sys.stdin.readline().strip('\n')))
    
    # ans = bfs(board, 10)
    r, c = find_empty(board)
    ans = dfs(board, r, c, 0, limit)

    if ans != -1:
        print("Solvable in {} move(s).".format(ans))
    else:
        print("Unsolvable in less than {} move(s).".format(limit))
