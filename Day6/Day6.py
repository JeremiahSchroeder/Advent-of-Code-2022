from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputString = inputFile.readlines()[0]

    inputFile.close()

    numCharacters = len(inputString)

    buffer = 0

    i=3
    while buffer ==0 :
        chars = inputString[i-3]
        for j in range(-2,1):
            if inputString[i+j] in chars:
                break
            else:
                chars += inputString[i+j]
        if len(chars) == 4:
            buffer = i+1
            break
        i+=1

    print(buffer)

    bufferMessage = 0
    markerLength = 14
    i=markerLength-1
    while bufferMessage ==0 :
        chars = inputString[i-(markerLength-1)]
        for j in range(-(markerLength-2),1):
            if inputString[i+j] in chars:
                break
            else:
                chars += inputString[i+j]
        if len(chars) == markerLength:
            bufferMessage = i+1
            break
        i+=1

    print(bufferMessage)




start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)