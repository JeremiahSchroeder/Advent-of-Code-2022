from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows = len(inputStringList)

    countTotalOverlap = 0
    countAnyOverlap = 0

    for i in range(0 , numRows):
        min1 = int(inputStringList[i].split(',')[0].split('-')[0])
        max1 = int(inputStringList[i].split(',')[0].split('-')[1])
        min2 = int(inputStringList[i].split(',')[1].split('-')[0])
        max2 = int(inputStringList[i].split(',')[1].split('-')[1].replace('\n',''))

        if ( min1 <= min2 and max1 >= max2 ) or ( min2 <= min1 and max2 >= max1 ):
            countTotalOverlap += 1

        if (min1 > min2 and min1 < max2 or
        min2 > min1 and min2 < max1 or
        max1 > min2 and max1 < max2 or
        max2 > min1 and max2 < max1  or
        min1 == min2 or
        min1 == max2 or
        max1 == min2 or
        max1 == max2):
            countAnyOverlap +=1




    print(countTotalOverlap)
    print(countAnyOverlap)




start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)