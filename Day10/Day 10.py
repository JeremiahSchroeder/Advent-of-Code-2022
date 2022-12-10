from time import sleep, perf_counter
import numpy



def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    for i in range(0,numRows):
        inputStringList[i]=inputStringList[i].replace('\n','')

    signalCycles = [20, 60, 100, 140, 180, 220]

    pixels = []

    signalStrength = []
    x = 1
    cycle =1

    for command in inputStringList:

        if cycle in signalCycles:
            signalStrength.append(cycle*x)

        if abs(x-(cycle-1)%40) < 2:
            pixels.append('#')
        else:
            pixels.append('.')

        cycle +=1

        if command.split(' ')[0] == 'addx':
            if cycle in signalCycles:
                signalStrength.append(cycle * x)

            if abs(x - (cycle - 1)%40) < 2:
                pixels.append('#')
            else:
                pixels.append('.')

            x += int(command.split(' ')[1])
            cycle+=1


    print(sum(signalStrength))

    print(pixels)

    for i in range(0,6):
        line = ''
        for j in range(0,40):
            line+= pixels[i*40+j]
        print(line)




start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)