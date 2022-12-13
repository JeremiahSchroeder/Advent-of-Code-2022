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

    left=[]
    right=[]

    for i in range(0, numRows):
        if i%3 == 0:
            left.append(stringToList(inputStringList[i],0))
        elif i%3 ==1:
            right.append(stringToList(inputStringList[i], 0))

    numPackets = len(left)

    # outputFile = open('testOutput', 'w')
    # for i in range(numPackets):
    #     outputFile.write(str(left[i]).replace(' ',''))
    #     outputFile.write('\n')
    #     outputFile.write(str(right[i]).replace(' ',''))
    #     outputFile.write('\n\n')
    #
    # outputFile.close()

    sumOfIndices = 0
    for i in range(numPackets):
        if comparePackets(left[i],right[i],0):
            sumOfIndices += i+1

    print(sumOfIndices)

    dividerPackets =[[[2]], [[6]]]

    listOfPackets = left + right + dividerPackets

    sortedPackets = []
    for packet in listOfPackets:
        if len(sortedPackets) == 0:
            sortedPackets = packet

        for i in range(0, len(sortedPackets)):
            if i < len(sortedPackets)-1:
                if comparePackets(packet,sortedPackets[i],0) and comparePackets(packet,sortedPackets[i+1],0):
                    sortedPackets.insert(i,packet)
                    break
            else:
                if comparePackets(packet,sortedPackets[i],0):
                    sortedPackets.insert(i, packet)
                else:
                    sortedPackets.append(packet)

    print((sortedPackets.index(dividerPackets[0])+1)*(sortedPackets.index(dividerPackets[1])+1))

def stringToList(packetString,depth):

    numChars = len(packetString)

    packetList = []

    i = 0

    while i <numChars:
        if packetString[i] == '[':
            level = 1
            for j in range(i+1,numChars):
                if packetString[j] == '[':
                    level +=1
                elif packetString[j] ==']':
                    level -=1
                    if level == 0:
                        endIndex = j
                        break
            if depth == 0:
                packetList = stringToList(packetString[i+1:endIndex],depth+1)

            else:
                packetList.append(stringToList(packetString[i+1:endIndex], depth+1))


            i = endIndex
        elif packetString[i] != ',':
            integerstring = packetString[i:].split(',')[0].split('[')[0].split(']')[0]
            packetList.append(int(integerstring))
            i += len(integerstring)-1

        i += 1

    return(packetList)

def comparePackets(leftPacket,rightPacket, depth):

    for i in range(0,len(leftPacket)):
        if i == len(rightPacket):
            return 0

        returnValue = None

        if type(leftPacket[i]) == list and type(rightPacket[i]) == list:
            returnValue = comparePackets(leftPacket[i],rightPacket[i],depth+1)
        elif type(leftPacket[i]) != list and type(rightPacket[i]) == list:
            returnValue = comparePackets([leftPacket[i]],rightPacket[i],depth+1)
        elif type(leftPacket[i]) == list and type(rightPacket[i]) != list:
            returnValue = comparePackets(leftPacket[i],[rightPacket[i]],depth+1)
        else:
            if leftPacket[i] < rightPacket[i]:
                return 1
            if leftPacket[i] > rightPacket[i]:
                return 0

        if returnValue == 0:
            return 0
        if returnValue == 1:
            return 1

    if len(rightPacket)>len(leftPacket) or depth == 0:
        return 1













start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)