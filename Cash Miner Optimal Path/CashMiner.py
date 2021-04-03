from datetime import datetime, timedelta

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
WALL = 'N'
EXIT = 'E'

MDIR = [DOWN, RIGHT, LEFT]

class Board:
    def __init__(self, fileName):
        self.epsilon = 0.001
        self.loadInput(fileName)
        self.iteration = 0
        self.start=datetime.now()
        self.limit=timedelta(seconds=29)
        
    def loadTiles(self, f, t, isExit):
        n = self.n
        lineArray = [None]*3
        numOfTile = int(f.readline())
        for i in range(numOfTile):
            line = f.readline()
            lineArray = map(int,(line.strip()).split(','))
            row = lineArray[0] - 1
            col = lineArray[1] - 1
            s = row * n + col
            self.action_board[s] = t
            if isExit :
                self.value_board[s] = lineArray[2]

    def moveTwoDementArray(self, s, row, col):
        return s + (self.n * row) + col

    def buildActionsPerTile(self):
        n = self.n
        nn = self.nn
        ab = self.action_board
        apt = self.action_per_tile = [None] * nn

        for s in self.rNNS:
            t = ab[s]
            
            up = [
                self.moveTwoDementArray(s, -1, -1),
                self.moveTwoDementArray(s, -1, 0),
                self.moveTwoDementArray(s, -1, 1),
            ]
            if s < n:
                up[0] = up[1] = up[2] = s
            elif (s + 1) % n == 0:   # right end of row
                up[2] = s
            elif s % n == 0:        # left end of row
                up[0] = s

            # Down
            down = [
                self.moveTwoDementArray(s, 1, -1),
                self.moveTwoDementArray(s, 1, 0),
                self.moveTwoDementArray(s, 1, 1),
            ]
            if s + n >= self.nn:
                down[0] = down[1] = down[2] = s
            elif (s + 1) % n == 0:  # right end of row
                down[2] = s
            elif s % n == 0:        # left end of row
                down[0] = s

            # Left
            left = [
                self.moveTwoDementArray(s, -1, -1),
                self.moveTwoDementArray(s, 0, -1),
                self.moveTwoDementArray(s, 1, -1)
            ]
            if s % n == 0:
                left[0] = left[1] = left[2] = s
            elif s + n >= self.nn: # Last row
                left[2] = s
            elif s < self.n:
                left[0] = s        # First row

            # Right
            right = [
                self.moveTwoDementArray(s, -1, +1),
                self.moveTwoDementArray(s, 0, +1),
                self.moveTwoDementArray(s, 1, +1)
            ]
            if (s + 1) % n == 0:
                right[0] = right[1] = right[2] = s
            elif s + n >= self.nn:          # Last row
                right[2] = s
            elif s < self.n:
                right[0] = s        # First row

            apt[s] = [up, down, left, right]
            for abd in apt[s] :
                for i in range(len(abd)):
                    if WALL == self.action_board[abd[i]]:
                        abd[i] = s

    def loadInput(self, path):
        f = open(path,'r')
        self.n = n = int(f.readline())
        self.nn = nn = n * n
        
        self.action_board = [RIGHT]*nn
        self.value_board = [0]*(nn)
        

        self.loadTiles(f, WALL, False)
        self.loadTiles(f, EXIT, True)

        # set rangNN Without WALL and EXIT
        self.rangeNN = range(self.nn)
        self.rNNS = filter(lambda s: self.action_board[s] != WALL and self.action_board[s] != EXIT, self.rangeNN)


        self.p = float(f.readline())
        self.p_wind = (1-self.p)/2
        self.r = float(f.readline())
        self.discount_factor = float(f.readline())

        f.close()
        
        self.buildActionsPerTile()

        self.delta = (self.epsilon * (1 - self.discount_factor) / self.discount_factor)
        
    def run(self):
        ab = self.action_board
        vb = self.value_board
        p = self.p
        p_wind = self.p_wind
        apt = self.action_per_tile
        rNNS = self.rNNS
        r = self.r
        df = self.discount_factor

        while True:
            maxDelta = 0

            for s in rNNS:
                cabd = apt[s][UP]
                maxValue =  (
                    vb[cabd[1]] * p + 
                    p_wind * (vb[cabd[0]] + vb[cabd[2]])
                )
                maxD = UP
                
                for d in MDIR:
                    cabd = apt[s][d]    
                    v =  (
                        vb[cabd[1]] * p + 
                        p_wind * (vb[cabd[0]] + vb[cabd[2]])
                    )
                    if v > maxValue:
                        maxValue = v
                        maxD = d

                maxV = r + (maxValue * df)
                
                delta = abs(maxV - vb[s])
                vb[s] = maxV
                ab[s] = maxD
                
                if delta > maxDelta :
                    maxDelta = delta

            self.iteration = self.iteration + 1
            self.end=datetime.now() - self.start
            avgtime = self.end / self.iteration
            
            if (self.limit - self.end) <= (avgtime)  or maxDelta < self.delta :
                return
            

    def printBoards(self):
        print "============================"
        '''
        print "PI Board"
        print self.getActionBoardPrint()
        '''
        print self.iteration, " Iteration"
        print "Runtime : ", self.end
    
    def saveFile(self):
        result = self.getActionBoardPrint()
        w = open("output.txt", "w+")
        w.write(result)
        w.close()
    
    def getActionBoardPrint(self):
        ab = self.action_board
        result = ''
        n = self.n
        for s in self.rangeNN: 
            col = s % n
            a = ab[s]

            if a == UP:
                a = 'U'
            elif a == DOWN:
                a = 'D'
            elif a == LEFT:
                a = 'L'
            elif a == RIGHT:
                a = 'R'

            result += a
            if col < n -1:
                result += ','
            else:
                result += '\n'
        return result

board = Board('input.txt')
board.run()
board.saveFile()