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

    directory = []
    directirySize = []

    for i in range(0,numRows):
        line = inputStringList[i].split(' ')
        if line[0] == '$' and line[1] == 'cd' and line[2] != '..':
            directory.append(line[2])
            directirySize.append(sumFilesInDirectory(inputStringList,i))

    sumSmallDirectories = 0
    for size in directirySize:
        if size <=100000:
            sumSmallDirectories += size

    print(sumSmallDirectories)

    spaceAvailable = totalSpace - directirySize[0]
    spaceToDelete = neededSpace - spaceAvailable

    directirySize.sort()

    tooSmall = True

    for size in directirySize:
        if size >= spaceToDelete:
            print(size)
            break


def sumFilesInDirectory(inputStringList,startIndex):
    directorySize = 0

    depth = 1
    stepIndex = 1
    while depth !=0 :
        index = stepIndex+startIndex
        if index >=len(inputStringList):
            break
        line = inputStringList[index].split(' ')
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    depth -=1
                else:
                    depth +=1

        elif line[0] != 'dir':
            directorySize += int(line[0])

        stepIndex+=1

    return directorySize





start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)