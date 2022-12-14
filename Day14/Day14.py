from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    for i in range(0,numRows):
        inputStringList[i]=inputStringList[i].replace('\n','')

    formationList = stringListToFormationList(inputStringList)
    boundaries = findBoundaries(formationList)

    rockLocations = findRockLocations(formationList)

    print(sandFall(rockLocations,boundaries))

    floor = boundaries[3]+2

    # print(sandFallwithFloor(rockLocations,floor))

    maxPossible = findMaxPossible(floor)

    rockAndGapLocations = rockLocations.copy()

    print(removeRocksAndGaps(rockAndGapLocations,floor,maxPossible))

def findMaxPossible(floor):
    maxPossible = 0
    for i in range (0,floor):
        maxPossible+= i*2+1

    return maxPossible

def removeRocksAndGaps(rockandGapLocations,floor,maxPossible):
    for j in range (0,floor):
        for i in range(500-j,501+j):
            if ((i,j) in rockandGapLocations or
                ((i - 1, j - 1) in rockandGapLocations and
                 (i, j - 1) in rockandGapLocations and
                 (i + 1, j - 1) in rockandGapLocations)):
                maxPossible -=1
                rockandGapLocations.append((i,j))

    return maxPossible

def stringListToFormationList(inputStringList):
    formationList = []
    for inputString in inputStringList:
        formationList.append(stringToTupleList(inputString))

    return formationList

def stringToTupleList(inputString):
    splitString = inputString.split(' -> ')

    tupleList = []
    for string in splitString:
        tupleList.append((int(string.split(',')[0]),int(string.split(',')[1])))

    return(tupleList)

def findBoundaries(formationList):
    xMin = 500
    xMax = 500
    yMax = 0
    yMin = 0
    for formation in formationList:
        for formationTuple in formation:
            xMin = min([formationTuple[0],xMin])
            xMax = max([formationTuple[0], xMax])
            yMax = max([formationTuple[1], yMax])

    return [xMin,xMax,yMin,yMax]

def findRockLocations(formationList):
    rockLocations = []

    for formation in formationList:
        numTuples = len(formation)

        for i in range(0,numTuples -1):
            start = formation[i]
            end = formation[i+1]

            if start[0] == end[0]:
                for j in range(0,int(end[1]-start[1]+(end[1]-start[1])/abs(end[1]-start[1])),int((end[1]-start[1])/abs(end[1]-start[1]))):
                    location = (start[0],start[1]+j)
                    if not location in rockLocations:
                        rockLocations.append(location)
            else:
                for j in range(0,int(end[0]-start[0]+(end[0]-start[0])/abs(end[0]-start[0])),int((end[0]-start[0])/abs(end[0]-start[0]))):
                    location = (start[0]+j,start[1])
                    if not location in rockLocations:
                        rockLocations.append(location)
    return rockLocations

def isInBounds(sandLocation, boundaries):
    return (sandLocation[0] >= boundaries[0]
                and sandLocation[0] <= boundaries[1]
                and sandLocation[1] <= boundaries[3])

def singleSandFall(sandLocations,rockLocations,boundaries):
    sandLocation = (500,0)

    falling = True

    while falling and isInBounds(sandLocation,boundaries):
        newLocation = (sandLocation[0],sandLocation[1]+1)

        if not (newLocation in sandLocations or newLocation in rockLocations):
            sandLocation = newLocation
        else:
            newLocation = (sandLocation[0]-1,sandLocation[1]+1)
            if not (newLocation in sandLocations or newLocation in rockLocations):
                sandLocation = newLocation
            else:
                newLocation = (sandLocation[0] + 1, sandLocation[1] + 1)
                if not (newLocation in sandLocations or newLocation in rockLocations):
                    sandLocation = newLocation
                else:
                    falling = False

    # print(sandLocation)
    isIntoAbyss = not isInBounds(sandLocation,boundaries)

    if not isIntoAbyss:
        sandLocations.append(sandLocation)

    return isIntoAbyss

def singleSandFallwithFloor(sandLocations,rockLocations,floor):
    sandLocation = (500,0)

    falling = True
    plugged = False

    while falling and not plugged:
        newLocation = (sandLocation[0],sandLocation[1]+1)

        if newLocation[1] == floor:
            falling = False
            break

        if not (newLocation in sandLocations or newLocation in rockLocations):
            sandLocation = newLocation
        else:
            newLocation = (sandLocation[0]-1,sandLocation[1]+1)
            if not (newLocation in sandLocations or newLocation in rockLocations):
                sandLocation = newLocation
            else:
                newLocation = (sandLocation[0] + 1, sandLocation[1] + 1)
                if not (newLocation in sandLocations or newLocation in rockLocations):
                    sandLocation = newLocation
                else:
                    falling = False


    if sandLocation[1] == 0:
        plugged = True
    sandLocations.append(sandLocation)

    return plugged

def sandFall(rockLocations,boundaries):

    sandLocations = []
    isIntoAbyss = False

    while not isIntoAbyss:
        isIntoAbyss = singleSandFall(sandLocations,rockLocations,boundaries)

    return(len(sandLocations))

def sandFallwithFloor(rockLocations, floor):

    sandLocations = []
    plugged = False

    height = floor
    while not plugged:
        plugged = singleSandFallwithFloor(sandLocations,rockLocations,floor)
        if sandLocations[-1][1] < height:
            height = sandLocations[-1][1]
            print(height)

    return(len(sandLocations))

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)