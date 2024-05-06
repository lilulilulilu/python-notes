
def get_live_neighbors(board, i, j):
    s = 0
    i_start, i_end = i-1, i+2
    j_start, j_end = j-1, j+2
    if i-1 < 0:
        i_start = 0
    if i + 1 >= m:
        i_end = m
    if j - 1 < 0:
        j_start = 0
    if j + 1 >= n:
        j_end = n
    for k in range(i_start, i_end):
        for h in range(j_start, j_end):
            if board[k][h] == '0' or board[k][h] == 1:
                s = s + 1
    return s - board[i][j]

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
m = len(board)
n = len(board[0])
for i in range(m):
    for j in range(n):
        live_neighbors = get_live_neighbors(board, i, j)
        print(f"(i,j):({i},{j})live_neighbors:{live_neighbors}")