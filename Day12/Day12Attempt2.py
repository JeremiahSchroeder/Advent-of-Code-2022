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

    numCol = len(inputStringList[0])

    topoMap = numpy.full((numRows, numCol),0)



    for i in range(0, numRows):
        for j in range(0, numCol):
            string = inputStringList[i][j]
            if string == 'S':
                topoMap[i,j] = 1
                startLocation = (i,j)
            elif string == 'E':
                topoMap[i,j] = 26
                endLocation = (i,j)
            else:
                topoMap[i,j] = ord(string) - 96


    neighborsArray = findNeighbors(topoMap)

    distanceArray = numpy.full((numRows, numCol), numRows * numCol)

    distanceArray[startLocation] = 0

    minimizeDistances(distanceArray,neighborsArray)


    print('The minimum path from the start to the end  is: ', distanceArray[endLocation])

    possibleStarts = getAllStarts(topoMap)

    print('The minimum possible path from elevation a to the end is: ', findShortestHike(possibleStarts,neighborsArray, endLocation))

def findShortestHike(possibleStarts,neighborsArray,endLocation):
    [numRows, numCol] = numpy.shape(neighborsArray)

    minPathDistance = numRows * numCol

    print('There are ', len(possibleStarts), ' possible starting locations')

    i = 0
    for start in possibleStarts:
        i+=1
        print('Checking location ', i)
        distanceArray = numpy.full((numRows, numCol), numRows * numCol)
        distanceArray[start] = 0
        minimizeDistances(distanceArray, neighborsArray)
        distance = distanceArray[endLocation]

        minPathDistance = min([minPathDistance, distance])

    return(minPathDistance)


def getAllStarts(topoMap):
    [numRows,numCol] = numpy.shape(topoMap)

    possibleStarts = []
    for i in range(0, numRows):
        for j in range(0, numCol):
            if topoMap[i][j] == 1:
                possibleStarts.append((i,j))
    return possibleStarts

def getEndLocation(topoMap):
    [numRows,numCol] = numpy.shape(topoMap)


    for i in range(0, numRows):
        for j in range(0, numCol):
            if topoMap[i][j] == 27:
                return (i,j)

def findNeighbors(topoMap):
    [numRows, numCol] = numpy.shape(topoMap)

    neighborsArray = numpy.empty([numRows,numCol], dtype=object)
    neighborsArray[0,0] = []

    for i in range(0,numRows):
        for j in range(0,numCol):
            neighborsArray[i, j] = []
            possibleNeighbors = [(i-1,j),
                              (i+1,j),
                              (i,j-1),
                              (i,j+1)]

            for neighbor in possibleNeighbors:
                if (    neighbor[0] > -1 and
                        neighbor[0] < numRows and
                        neighbor[1] >-1 and
                        neighbor[1] < numCol and
                        topoMap[neighbor]-topoMap[i,j] <= 1):
                        neighborsArray[i,j].append(neighbor)

    return neighborsArray

def updateDistance(distanceArray, neighborsArray):
    [numRows, numCol] = numpy.shape(distanceArray)

    updated = False

    for i in range(0,numRows):
        for j in range(0,numCol):
            neighbors = neighborsArray[i,j]
            for neighbor in neighbors:
                if  distanceArray[neighbor] > distanceArray[i,j]+1:
                    distanceArray[neighbor] = distanceArray[i,j]+1
                    updated = True


    return updated

def minimizeDistances(distanceArray, neighborsArray):
    updated = True

    while updated :
        updated= updateDistance(distanceArray,neighborsArray)


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)