from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    row = 2000000
    areaLimit = 4000000
    # inputFile = open('inputTest','r')
    # row = 10
    # areaLimit = 20

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    for i in range(0,numRows):
        inputStringList[i]=inputStringList[i].replace('\n','')

    [sensorCoordinates, beaconCoordinates, distances] = findCoordinates(inputStringList)


    print(findBeaconFreeRanges(sensorCoordinates,beaconCoordinates,distances,row))

    print(checkAllPerimeters(sensorCoordinates,distances,areaLimit))

def findCoordinates(inputStringList):

    sensorCoordinates = []
    beaconCoordinates = []
    distances = []

    for inputString in inputStringList:
        sensorX = int(inputString.split(' ')[2].replace('x=','').replace(',',''))
        sensorY = int(inputString.split(' ')[3].replace('y=','').replace(':',''))

        sensorCoordinates.append((sensorX,sensorY))

        beaconX = int(inputString.split(' ')[8].replace('x=','').replace(',',''))
        beaconY = int(inputString.split(' ')[9].replace('y=', ''))

        if not (beaconX,beaconY) in beaconCoordinates:
            beaconCoordinates.append((beaconX,beaconY))

        distances.append(abs(sensorX-beaconX)+abs(sensorY-beaconY))

    return[sensorCoordinates,beaconCoordinates,distances]

def findBeaconFreeRanges(sensorCoordinates,beaconCoordinates,distances,row):

    numSensors = len(sensorCoordinates)
    overlappedFreeRanges = []

    for i in range(0,numSensors):
        sensorCoordinate = sensorCoordinates[i]
        distance = distances[i]

        if abs(row-sensorCoordinate[1])<=distance:

            numFreeInRow = 2*(distance-abs(row-sensorCoordinate[1]))+1

            startX = sensorCoordinate[0]-(numFreeInRow-1)//2
            endX = sensorCoordinate[0]+(numFreeInRow-1)//2

            overlappedFreeRanges.append([startX,endX])

    overlappedFreeRanges.sort()

    freeRanges = []

    for overlappedRange in overlappedFreeRanges:
        if len(freeRanges) == 0:
            freeRanges.append(overlappedRange)
        else:
            if overlappedRange[0] <= freeRanges[-1][1] and overlappedRange[1] > freeRanges[-1][1]:
                freeRanges[-1] = [freeRanges[-1][0], overlappedRange[1]]
            elif overlappedRange[0] > freeRanges[-1][1]:
                freeRanges.append(overlappedRange)

    numFree = 0
    for freeRange in freeRanges:
        numFree += freeRange[1]-freeRange[0]+1
    for beaconCoordinate in beaconCoordinates:
        if beaconCoordinate[1] == row:
            for freeRange in freeRanges:
                if beaconCoordinate[0] >= freeRange[0] and beaconCoordinate[0] <= freeRange[1]:
                    numFree -= 1

                    break

    return numFree

def checkperimeter(index,sensorCoordinates,distances,areaLimit):
    print('in CheckPerimeter with index ',index)
    distanceOutOfRange = distances[index]+1
    sensorCoordinate = sensorCoordinates[index]

    for i in range (0, distanceOutOfRange):
        currentPoint = (sensorCoordinate[0] + distanceOutOfRange - i, sensorCoordinate[1] +i)

        tuningFrequency = checkRange(sensorCoordinates,distances,areaLimit,currentPoint)

        if tuningFrequency != -1:
            return tuningFrequency

        currentPoint = (sensorCoordinate[0] + distanceOutOfRange - i, sensorCoordinate[1] - i)

        tuningFrequency = checkRange(sensorCoordinates, distances, areaLimit, currentPoint)

        if tuningFrequency != -1:
            return tuningFrequency

        currentPoint = (sensorCoordinate[0] - distanceOutOfRange + i, sensorCoordinate[1] + i)

        tuningFrequency = checkRange(sensorCoordinates, distances, areaLimit, currentPoint)

        if tuningFrequency != -1:
            return tuningFrequency

        currentPoint = (sensorCoordinate[0] - distanceOutOfRange + i, sensorCoordinate[1] - i)

        tuningFrequency = checkRange(sensorCoordinates, distances, areaLimit, currentPoint)

        if tuningFrequency != -1:
            return tuningFrequency
    return -1

def checkRange(sensorCoordinates,distances,areaLimit,currentPoint):

    outOfRange = True

    if currentPoint[0] < 0 or currentPoint[0] > areaLimit or currentPoint[1] < 0 or currentPoint[1] > areaLimit:
        return -1

    for j in range(0, len(sensorCoordinates)):
        if abs(sensorCoordinates[j][0] - currentPoint[0]) + abs(sensorCoordinates[j][1] - currentPoint[1]) <= distances[
            j]:
            outOfRange = False
            break

    if outOfRange:
        return currentPoint[0] * 4000000 + currentPoint[1]
    else:
        return -1

def checkAllPerimeters(sensorCoordinates,distances,areaLimit):
    for index in range(0,len(sensorCoordinates)):
        tuningFrequency = checkperimeter(index, sensorCoordinates, distances, areaLimit)
        if tuningFrequency != -1:
            return tuningFrequency
    return tuningFrequency


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)