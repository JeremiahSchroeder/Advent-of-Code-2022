from time import sleep, perf_counter
import numpy

worryLevels = []
operation = []
operationValue = []
test = []
throwToIfTrue = []
throwToIfFalse = []
inspections = []

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    for i in range(0,numRows):
        inputStringList[i]=inputStringList[i].replace('\n','')

    numCol = len(inputStringList[0])

    topoMap = numpy.full((numRows, numCol),0)

    for i in range(0, numRows):
        for j in range(0, numCol):
            string = inputStringList[i][j]
            if string == 'S':
                topoMap[i,j] = 0
            elif string == 'E':
                topoMap[i,j] = 27
            else:
                topoMap[i,j] = ord(string) - 96

    path = [getStartLocation(topoMap)]

    print(searchPath(path,topoMap))

def getStartLocation(topoMap):
    [numRows,numCol] = numpy.shape(topoMap)
    numCols = len(topoMap)

    for i in range(0, numRows):
        for j in range(0, numCols):
            if topoMap[i][j] == 0:
                return (i,j)

def searchPath(path,topoMap):

    [numRows,numCol] = numpy.shape(topoMap)

    r = path[-1][0]
    c = path[-1][1]

    currentEl = topoMap[r,c]

    possibleMoves = [(r + (r != numRows -1 ) , c),
                     (r - (r != 0), c),
                     (r, c + (c != numCol - 1)),
                     (r, c - (c != 0))]

    pathLengths = []

    goalElevation = currentEl

    for possibleMove in possibleMoves:
        if topoMap[possibleMove] == goalElevation +1:
            goalElevation +=1
            break

    for possibleMove in possibleMoves:
        newEl = topoMap[possibleMove]

        if  (not possibleMove in path) and newEl == goalElevation:
            newPath = path.copy()
            newPath.append(possibleMove)
            if newEl == 27:
                return len(newPath)-1
            else:
                pathLengths.append(searchPath(newPath,topoMap))

    if len(pathLengths) == 0:
        return numRows*numCol
    else:
        return(min(pathLengths))





start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)