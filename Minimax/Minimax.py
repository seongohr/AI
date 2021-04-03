import copy

BLANK = 0
PLAYER_EMMITER = 1
OPPONENT_EMMITER = 2
WALL = 3
PLAYER_LAY = 10
OPPONENT_LAY = 20
LAY_LENGTH = 3

MAX_DEPTH = 4
BOARD_SIZE = 4

MAX_SCORE = 9999999
MIN_SCORE = -9999999

LAYMAP = [
    (-1,0), (-2,0), (-3,0),
    (1,0), (2,0), (3,0),
    (0,1), (0,2), (0,3),
    (0,-1), (0,-2), (0,-3),
    (-1,-1), (-2,-2), (-3,-3),
    (1,1), (2,2), (3,3),
    (1,-1), (2,-2), (3,-3),
    (-1,1), (-2,2), (-3,3),
]

# Load from file
def loadInput(path) :
    global BOARD_SIZE
    board = []
    f = open(path, 'r')
    BOARD_SIZE = int(f.readline())
    row = 0
    while True:
        line = f.readline()
        if not line: break
        #extract rows one by one
        oneRow = []
        for i in range(BOARD_SIZE):
            oneCell = int(line[i])
            oneRow.append(oneCell)
        board.append(oneRow)
        row = row + 1
    f.close()

    return board
    
def write_output(position):
    w = open("output.txt", "w+")
    w.write("" + str(position[0]) + " " + str(position[1]))
    w.close()

def getMoveablePositions(board) :
    positions = []
    x = 0    
    for row in board :
        y = 0
        for v in row :
            if v == 0 :
                positions.append((x,y))
            y = y + 1
        x = x + 1
    return positions

def layserMarkingOnBoard(board) :
    emmiters = []
    # find emmiters
    x = 0    
    for row in board :
        y = 0
        for v in row :
            if v == PLAYER_EMMITER or v == OPPONENT_EMMITER:
                emmiters.append((x,y))   #row, col         
            y = y + 1
        x = x + 1
    
    # Marking on Board
    for emmiter in emmiters :
        markOneEmmiterOnBoard(board, emmiter, board[emmiter[0]][emmiter[1]])

def markOneEmmiterOnBoard(board, pos, emmiter) :
    x = pos[0]
    y = pos[1]
    board[x][y] = emmiter

    for dpos in LAYMAP :
        c_x = x + dpos[0]
        c_y = y + dpos[1]        
        
        if c_x < 0 or c_x >= BOARD_SIZE:
            continue
        if c_y < 0 or c_y >= BOARD_SIZE:
            continue

        c_v = board[c_x][c_y]

        if c_v == WALL :
            continue
        elif c_v == 0 :
            if emmiter == PLAYER_EMMITER :
                c_v = PLAYER_LAY
            else:
                c_v = OPPONENT_LAY
        elif c_v == PLAYER_LAY and emmiter == OPPONENT_EMMITER:
            c_v += OPPONENT_LAY
        elif c_v == OPPONENT_LAY and emmiter == PLAYER_EMMITER:
            c_v += PLAYER_LAY

        board[c_x][c_y] = c_v

def score(board) :
    oppent_score = 0
    player_score = 0
    for row in board:
        for val in row:
            if val == OPPONENT_LAY or val == OPPONENT_EMMITER :
                oppent_score += 1
            elif val == PLAYER_LAY or val == PLAYER_EMMITER :
                player_score += 1

    return player_score - oppent_score

def getMinMax(board, turn, depth) :
    moveable_pos = getMoveablePositions(board)

    if depth <= 0 or len(moveable_pos) == 0 :
        return score(board)

    if turn == PLAYER_EMMITER:
        return getMaxScore(board, depth)
    else:
        return getMinScore(board, depth)

def getMaxScore(board, depth) :
    best_score = MIN_SCORE

    for pos in getMoveablePositions(board) :
        new_board = copy.deepcopy(board)
        new_board[pos[0]][pos[1]] = PLAYER_EMMITER
        markOneEmmiterOnBoard(new_board, pos, PLAYER_EMMITER)
        new_score = getMinMax(new_board, OPPONENT_EMMITER, depth - 1)
        if new_score > best_score :
            best_score = new_score
    return best_score

def getMinScore(board, depth) :
    best_score = MAX_SCORE

    for pos in getMoveablePositions(board) :
        new_board = copy.deepcopy(board)
        new_board[pos[0]][pos[1]] = OPPONENT_EMMITER
        markOneEmmiterOnBoard(new_board, pos, OPPONENT_EMMITER)
        new_score = getMinMax(new_board, PLAYER_EMMITER, depth - 1)
        if new_score < best_score :
            best_score = new_score
    return best_score

def getBestPosition(board, depth) :
    best_position = (0,0)
    score = MIN_SCORE

    for pos in getMoveablePositions(board) :
        new_board = copy.deepcopy(board)
        new_board[pos[0]][pos[1]] = PLAYER_EMMITER
        layserMarkingOnBoard(new_board)
        new_score = getMinMax(new_board, OPPONENT_EMMITER, depth - 1)
        if new_score > score :
            score = new_score
            best_position = pos
    return best_position


board = loadInput('input.txt')
layserMarkingOnBoard(board)
bestpos = getBestPosition(board, MAX_DEPTH)
write_output(bestpos)
