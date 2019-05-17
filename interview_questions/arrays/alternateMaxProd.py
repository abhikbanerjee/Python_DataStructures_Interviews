import sys


def adjacentElementsProduct(inputArray):
    i=0
    maxProd = -1*sys.maxsize
    while i<len(inputArray)-1:
        prod = inputArray[i]*inputArray[i+1]
        if prod >= maxProd:
            maxProd=prod
        i+=1
    return maxProd


li = [-23, 4, -3, 8, -12]
print(adjacentElementsProduct(li))
