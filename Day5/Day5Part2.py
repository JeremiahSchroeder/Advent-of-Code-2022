from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    #Find empty row
    for i in range(0,numRows):
        # remove newline characters
        inputStringList[i]=inputStringList[i].replace('\n','')
        if inputStringList[i] == '':
            stackIndicesRow = i-1

    numberOfStacks = int(inputStringList[stackIndicesRow][-1])

    stackList = [[] for _ in range(numberOfStacks)]
    columnIndices = [0]*numberOfStacks

    for i in range(0,numberOfStacks):
        columnIndices[i] = inputStringList[stackIndicesRow].index(str(i+1))

    for i in range(stackIndicesRow-1,-1,-1):
        for j in range(0,numberOfStacks):
            columnIndex = columnIndices[j]
            if len(inputStringList[i])>= columnIndex:
                if inputStringList[i][columnIndex] != ' ':
                    stackList[j].append(inputStringList[i][columnIndex])

    for i in range(stackIndicesRow+2,numRows):
        numberToMove = int(inputStringList[i].split(' ')[1])
        originStack = int(inputStringList[i].split(' ')[3])
        destinationStack = int(inputStringList[i].split(' ')[5])

        for j in range(-numberToMove,0):
            stackList[destinationStack-1].append(stackList[originStack-1].pop(j))
    topLevelString = ''
    for i in range(0,numberOfStacks):
        topLevelString += stackList[i][-1]

    print(topLevelString)


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)