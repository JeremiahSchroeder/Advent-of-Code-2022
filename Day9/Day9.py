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

    tailPositions=[[0,0]]

    currentTailPosition = [0,0]
    currentHeadPosition = [0, 0]


    # printPosition(currentHeadPosition,currentTailPosition)
    for move in inputStringList:
        direction = move.split(' ')[0]
        numMoves = int(move.split(' ')[1])

        for i in range(0,numMoves):

            currentTailPosition = updatePositions(currentHeadPosition,currentTailPosition,direction)
            if not currentTailPosition in tailPositions:
                # print(currentTailPosition)
                tailPositions.append(currentTailPosition)
            # printPosition(currentHeadPosition,currentTailPosition)

    print(len(tailPositions))






def updatePositions(currentHeadPosition,currentTailPosition,direction):
    if direction == 'U':
        currentHeadPosition[0] += 1
    if direction == 'D':
        currentHeadPosition[0] -= 1
    if direction == 'R':
        currentHeadPosition[1] += 1
    if direction == 'L':
        currentHeadPosition[1] -= 1
    difference = numpy.subtract(currentHeadPosition,currentTailPosition)

    if abs(difference[0])<2 and abs(difference[1])<2:
        move = [0,0]
    elif difference[0] == 0 or difference[1] == 0:
        move = difference // 2
    else:
        move = [difference[0]//abs(difference[0]),difference[1]//abs(difference[1])]


    currentTailPosition = numpy.add(currentTailPosition, move)

    return list(currentTailPosition)

def printPosition(currentHeadPosition,currentTailPosition):
    grid = numpy.full((5,6),'.')
    print(currentHeadPosition)
    grid[currentTailPosition[0],currentTailPosition[1]] = 'T'
    grid[currentHeadPosition[0],currentHeadPosition[1]] = 'H'

    print(grid)
    print('\n')

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)