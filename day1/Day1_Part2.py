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

    elfIndex=0
    sumCaloriesList=[0]

    for i in range (0, numRows):
        if (inputStringList[i]==''):
            elfIndex +=1
            sumCaloriesList.append(0)
        else :
            sumCaloriesList[elfIndex] += int(inputStringList[i])

    sumCaloriesList.sort(reverse=True)
    sumTopThree = sum(sumCaloriesList[0:3])

    print(sumCaloriesList[0:3])
    print(sumTopThree)
start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)