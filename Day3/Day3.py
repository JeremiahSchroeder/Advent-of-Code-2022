from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    sumPriorities = 0

    for i in range (0, numRows):
        inputStringList[i]=inputStringList[i].replace('\n','')
        compartmentSize = int(len(inputStringList[i]) / 2)

        firstCompartment = inputStringList[i][0:compartmentSize]
        secondCompartment = inputStringList[i][compartmentSize:2*compartmentSize]

        for j in range (0, compartmentSize):
            if firstCompartment[j] in secondCompartment:
                sumPriorities += getPriority(firstCompartment[j])
                break

    print(sumPriorities)

    sumPriorities = 0
    for i in range (0, numRows, 3):
        for j in range(0, len(inputStringList[i])):
            if inputStringList[i][j] in inputStringList[i+1] and inputStringList[i][j] in inputStringList[i+2]:
                sumPriorities+= getPriority(inputStringList[i][j])
                break
    print(sumPriorities)

def getPriority(item):
    priority = ord(item)
    if(priority > 96):
        priority -= 96
    else :
        priority -= 38
    return priority

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)