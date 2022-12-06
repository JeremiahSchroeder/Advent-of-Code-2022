from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)
    points = 0
    pointsPart2 = 0

    for i in range (0, numRows):
        opp = inputStringList[i].split()[0]
        you = inputStringList[i].split()[1]
        youPart2 = yourPlay(opp,you)
        points += (winValue(opp,you)+playValue(you))
        pointsPart2 += (winValue(opp,youPart2)+playValue(youPart2))
    print(points)
    print(pointsPart2)

def winValue(opp,you):
    if (opp == 'A'):
        if (you == 'X'):
            return 3
        elif (you == 'Y'):
            return 6
        else :
            return 0
    elif (opp == 'B'):
        if (you == 'Y'):
            return 3
        elif (you == 'Z'):
            return 6
        else:
            return 0
    else:
        if (you == 'Z'):
            return 3
        elif (you == 'X'):
            return 6
        else:
            return 0

def playValue(you):
    if (you == 'X'):
        return 1
    elif (you == 'Y'):
        return 2
    else:
        return 3

def yourPlay(opp, strategy):
    if (opp == 'A'):
        if (strategy == 'X'):
            return 'Z'
        elif (strategy == 'Y'):
            return 'X'
        else :
            return 'Y'
    elif (opp == 'B'):
        if (strategy == 'X'):
            return 'X'
        elif (strategy == 'Y'):
            return 'Y'
        else:
            return 'Z'
    else:
        if (strategy == 'X'):
            return 'Y'
        elif (strategy == 'Y'):
            return 'Z'
        else:
            return "X"
start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)