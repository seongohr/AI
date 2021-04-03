
# Problem Config
landCnt = 0
gateCnt = 0
takeOffCnt = 0
numOfPlane = 0

PI_R = 0
PI_M = 1
PI_S = 2
PI_O = 3
PI_C = 4
planeInfo = []

# assignedtable define
AT_LAND_LANE = 0
AT_LAND_ENDTIME = 1
AT_GATE_NUM = 2
AT_TAKEOFFSTARTTIME = 3
AT_TAKEOFF_LANE = 4
AT_TAKEOFFENDTIME = 5
AT_LAND_STARTTIME = 6
assignedTable = []

def loadInput(path) :
    global landCnt, gateCnt, takeOffCnt, numOfPlane
    global planeInfo, assignedTable

    f = open(path, 'r')
    lgt = map(int,(f.readline().strip()).split(' '))
    numOfPlane=int(f.readline())
   
    #make given number of landing strip, gate, take off strip
    landCnt = lgt[0]
    gateCnt = lgt[1]
    takeOffCnt = lgt[2]

    #planeInfo = [R, M, S, O, C] : R-remaining hover mins, M-mins to land to gate, S-mininum mins to stay gate, 
    #                              O-mins to complete take off, C-Max mins to stay gate
    for i in range(numOfPlane):
        line = f.readline()
        #extract rows one by one
        oneRow = map(int, line.strip().split(' '))
        planeInfo.append(oneRow)
        # Generate Assigned Table
        assignedTable.append([-1] * 7)
    f.close()

# @return
def pickLandLane(assignedTable):
    pickedLandLane = -1
    landingAva = -1
    for laneNum in range(landCnt):
        ava = -1
        for at in assignedTable :
            if at[AT_LAND_LANE] == laneNum :
                if ava < at[AT_LAND_ENDTIME] :
                    ava = at[AT_LAND_ENDTIME]
        if ava == -1 :
            pickedLandLane = laneNum
            landingAva = 0
            break
        elif pickedLandLane == -1 or landingAva > ava:
            pickedLandLane = laneNum
            landingAva = ava
    
    return pickedLandLane, landingAva

def pickGate(assignedTable) :
    pickedGate = -1
    landingAva = -1
    for gateNum in range(gateCnt):
        isNotAva = False
        ava = -1
        for at in assignedTable :
            if at[AT_GATE_NUM] == gateNum:
                if  at[AT_TAKEOFFSTARTTIME] == -1:
                    isNotAva = True
                    break
                if ava < at[AT_TAKEOFFSTARTTIME] :
                    ava = at[AT_TAKEOFFSTARTTIME]
        if isNotAva == True:
            continue     
        elif ava == -1 :
            pickedGate = gateNum
            landingAva = 0
            break
        elif pickedGate == -1 or landingAva > ava:
            pickedGate = gateNum
            landingAva = ava
    
    return pickedGate, landingAva

def getLandingPlanes(assignedTable) :
    ret = []

    def compare(a,b) :
        pa = planeInfo[a]
        pb = planeInfo[b]
        return (pa[PI_R] + pa[PI_M]) - (pb[PI_R] + pb[PI_M])

    for i in range(numOfPlane) :
        if assignedTable[i][AT_LAND_LANE] == -1 :
            ret.append(i)

    return sorted(ret, cmp = compare)

def pickTakeOffLane(assignedTable) :
    pickedTakeOffLane = -1
    TakeOffAva = -1
    for takeOffLane in range(takeOffCnt):
        ava = -1
        for at in assignedTable :
            if at[AT_TAKEOFF_LANE] == takeOffLane :
                if ava < at[AT_TAKEOFFENDTIME] :
                    ava = at[AT_TAKEOFFENDTIME]
        if ava == -1 :
            pickedTakeOffLane = takeOffLane
            TakeOffAva = 0
            break
        elif pickedTakeOffLane == -1 or TakeOffAva > ava:
            pickedTakeOffLane = takeOffLane
            TakeOffAva = ava
    
    return pickedTakeOffLane, TakeOffAva

def getTakeoffPlanes(assignedTable) :
    ret = []

    def compare(a,b) :
        pa = planeInfo[a]
        ascore = assignedTable[a][AT_LAND_ENDTIME] + pa[PI_S] + pa[PI_C] + pa[PI_O]
        pb = planeInfo[b]
        bscore = assignedTable[b][AT_LAND_ENDTIME] + pb[PI_S] + pb[PI_C] + pb[PI_O]
        return (ascore - bscore)

    for i in range(numOfPlane) :
        if assignedTable[i][AT_GATE_NUM] != -1 and assignedTable[i][AT_TAKEOFF_LANE] == -1 :
            ret.append(i)

    return sorted(ret, cmp = compare)

def process(assignedTable) :

    # Check it is completed
    isSuccess = True
    for at in assignedTable :
        if at[AT_TAKEOFFENDTIME] == -1:
            isSuccess = False
            break
    if isSuccess :
        return True
    
    # Finding avaliable landing lane and gate and takeoff lane
    pickedLandLane, laneLandingAva = pickLandLane(assignedTable)
    pickedGate, gateLandingAva = pickGate(assignedTable)
    pickedTakeoffLane, takeoffava = pickTakeOffLane(assignedTable)

    if pickedGate != -1 :
        # landing Start
        priorityOfPlanes = getLandingPlanes(assignedTable)
        for planeNum in priorityOfPlanes :
            pi = planeInfo[planeNum]
            landingAva = gateLandingAva - pi[PI_M]
            if landingAva < laneLandingAva : 
                landingAva = laneLandingAva
             
            landEndTime = landingAva + pi[PI_M]
            if landEndTime + pi[PI_C] < takeoffava :
                difference = ( takeoffava - (landEndTime + pi[PI_C]) )
                landingAva = landingAva + difference
                landEndTime = landingAva + pi[PI_M]

            if planeInfo[planeNum][PI_R] < landingAva :
                return False

            assignedTable[planeNum][AT_LAND_LANE] = pickedLandLane
            assignedTable[planeNum][AT_GATE_NUM] = pickedGate
            assignedTable[planeNum][AT_LAND_STARTTIME] = landingAva
            assignedTable[planeNum][AT_LAND_ENDTIME] = landEndTime

            if process(assignedTable) == True :
                return True
            else : # Backtracking
                assignedTable[planeNum][AT_LAND_LANE] = -1
                assignedTable[planeNum][AT_GATE_NUM] = -1
                assignedTable[planeNum][AT_LAND_ENDTIME] = -1
                assignedTable[planeNum][AT_LAND_STARTTIME] = -1

    # Takeoff Start
    if pickedTakeoffLane != -1 :
        priorityOfPlanes = getTakeoffPlanes(assignedTable)
        for planeNum in priorityOfPlanes:
            # get takeoff start with plane
            at = assignedTable[planeNum]
            info = planeInfo[planeNum]
            possibleTakeOffStart = at[AT_LAND_ENDTIME] + info[PI_S]
            if possibleTakeOffStart < takeoffava :
                # if at[AT_LAND_ENDTIME] + info[PI_C] >= takeoffava :
                if  at[AT_LAND_ENDTIME] + info[PI_C] >= takeoffava :
                    possibleTakeOffStart = takeoffava
                else :
                    return False
            
            # assign to take off
            assignedTable[planeNum][AT_TAKEOFF_LANE] = pickedTakeoffLane
            assignedTable[planeNum][AT_TAKEOFFSTARTTIME] = possibleTakeOffStart
            assignedTable[planeNum][AT_TAKEOFFENDTIME] = possibleTakeOffStart + info[PI_O]
            
            if process(assignedTable) == True :
                return True
            
            assignedTable[planeNum][AT_TAKEOFF_LANE] = -1
            assignedTable[planeNum][AT_TAKEOFFSTARTTIME] = -1
            assignedTable[planeNum][AT_TAKEOFFENDTIME] = -1
    #sys.stdin.read(1)
    return False

# target input file
defaultPath = './input.txt'
#if len(sys.argv) == 2:
#    defaultPath = sys.argv[1]

# Loadinput test
loadInput(defaultPath)

if process(assignedTable) == False :
    print 'It can not landing safely...'
else :
    w = open("output.txt", "w+")
    for at in assignedTable:
        w.write("" + str(at[AT_LAND_STARTTIME]) + ' ' + str(at[AT_TAKEOFFSTARTTIME]) + '\n')
    w.close()

# print assignedTable

# print numOfPlane, AssignedTable
