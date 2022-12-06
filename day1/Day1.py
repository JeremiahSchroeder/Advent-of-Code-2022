from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    for i in range (0, numRows):
        inputStringList[i] = inputStringList[i].replace('\n','')

    maxCalories = 0
    sumCalories = 0

    for i in range (0, numRows):
        if (inputStringList[i]==''):
            sumCalories = 0
        else :
            sumCalories += int(inputStringList[i])
            if (sumCalories > maxCalories):
                maxCalories = sumCalories

    print(maxCalories)
start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)