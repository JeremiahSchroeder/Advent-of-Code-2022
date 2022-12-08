from time import sleep, perf_counter
import numpy

def solution():

    totalSpace = 70000000
    neededSpace = 30000000

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    for i in range(0,numRows):
        inputStringList[i]=inputStringList[i].replace('\n','')

    numColumns = len(inputStringList[0])


    numVisible = numRows*2 + (numColumns-2)*2
    maxScenicScore = 0

    for i in range (1,numRows-1):
        for j in range(1, numColumns-1):
            numVisible += isVisible(inputStringList,i,j)
            maxScenicScore = max([maxScenicScore, getScenicScore(inputStringList,i,j)])

    print(numVisible)

    print(maxScenicScore)


def isVisible(inputStringList,iInput,jInput):
    treeHeight = inputStringList[iInput][jInput]

    numRows = len(inputStringList)
    numColumns = len(inputStringList[0])


    i = iInput
    while i >0:
        i -=1

        if inputStringList[i][jInput] >= treeHeight:
            break
        if i == 0:
            return 1

    i = iInput
    while i <numRows:
        i +=1
        if inputStringList[i][jInput] >= treeHeight:
            break
        if i == numRows-1:
            return 1

    j = jInput
    while j >0:
        j -=1
        if inputStringList[iInput][j] >= treeHeight:
            break
        if j == 0:
            return 1
    j = jInput
    while j <numColumns:
        j +=1
        if inputStringList[iInput][j] >= treeHeight:
            break
        if j == numColumns-1:
            return 1
    return 0

def getScenicScore(inputStringList,iInput,jInput):
    treeHeight = inputStringList[iInput][jInput]
    numRows = len(inputStringList)
    numColumns = len(inputStringList[0])
    scenicScore = 1


    i = iInput
    while i >0:
        i -=1
        if inputStringList[i][jInput] >= treeHeight or i ==0:
            scenicScore *= (iInput-i)
            break

    i = iInput
    while i <numRows:
        i +=1
        if inputStringList[i][jInput] >= treeHeight or i == numRows-1:
            scenicScore *= (i-iInput)
            break

    j = jInput
    while j >0:
        j -=1
        if inputStringList[iInput][j] >= treeHeight or j ==0:
            scenicScore *= (jInput-j)
            break

    j = jInput
    while j <numColumns:
        j +=1
        if inputStringList[iInput][j] >= treeHeight or j == numColumns-1:
            scenicScore *= (j-jInput)
            break

    return scenicScore

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)