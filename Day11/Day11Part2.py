from time import sleep, perf_counter
import numpy

worryLevels = []
operation = []
operationValue = []
test = []
throwToIfTrue = []
throwToIfFalse = []
inspections = []

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    for i in range(0,numRows):
        inputStringList[i]=inputStringList[i].replace('\n','')

    rowsInInput = 7
    numMonkeys = numRows//rowsInInput + 1

    # print(inputStringList[1].split('Starting Items: ')[0])

    for i in range (0, numMonkeys):
        row=i*rowsInInput
        worryLevels.append(getWorriesFromStr(inputStringList[row+1]))
        if inputStringList[row+2].split(' ')[-1] == 'old':
            operation.append('squared')
            operationValue.append('1')
        else :
            operation.append(inputStringList[row+2].split(' ')[-2])
            operationValue.append(int(inputStringList[row+2].split(' ')[-1]))
        test.append(int(inputStringList[row+3].split(' ')[-1]))
        throwToIfTrue.append(int(inputStringList[row+4].split(' ')[-1]))
        throwToIfFalse.append(int(inputStringList[row+5].split(' ')[-1]))
        inspections.append(0)

    productOfTests = 1
    for testValue in test:
        productOfTests *= testValue


    for i in range(0,10000):
        monkeyRound(numMonkeys,productOfTests)


    print(getMonkeyBusiness())

def getWorriesFromStr(string):
    string = string.split('Starting items: ')[1]
    string = string.split(', ')

    worries = []

    for worry in string:
        worries.append( int(worry) )

    return worries

def monkeyThrow(monkeyIndex,productOfTests):
    while len(worryLevels[monkeyIndex]) > 0:
        inspections[monkeyIndex] +=1
        worry = worryLevels[monkeyIndex].pop(0)
        if operation[monkeyIndex] == '*':
            worry  *= operationValue[monkeyIndex]
        elif operation[monkeyIndex] == '+':
            worry += operationValue[monkeyIndex]
        else:
            worry *= worry

        # worry = worry // 3

        if worry%test[monkeyIndex] == 0:
            worryLevels[throwToIfTrue[monkeyIndex]].append(worry)
        else:
            worryLevels[throwToIfFalse[monkeyIndex]].append(worry%productOfTests)


def monkeyRound(numMonkeys,productOfTests):
    for i in range(0,numMonkeys):
        monkeyThrow(i,productOfTests)



def getMonkeyBusiness():
    inspectionsCopy = inspections.copy()
    monkeyBusiness = max(inspectionsCopy)
    inspectionsCopy.remove(monkeyBusiness)
    monkeyBusiness *= max(inspectionsCopy)

    return(monkeyBusiness)


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)