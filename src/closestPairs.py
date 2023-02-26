import numpy
from bruteForce import *

euclidCount = 0

def euclideanDistance(arr1 : numpy.array, arr2 : numpy.array):
    global euclidCount
    euclidCount += 1
    
    squared = numpy.square(arr1 - arr2)
    squared_sum = numpy.sum(squared)
 
    return numpy.sqrt(squared_sum)

def ClosestPair(points : numpy.array, n : int):
    closest = 0.0
    pointsPair = numpy.array([])
    
    if(n <= 3):
        return bruteForce(points, n)
    else:
        # case 1 : same side
        mid = int(n/2)
        left = points[0:mid]
        right = points[mid:n]

        # split into left and right
        leftPair, leftClosest, = ClosestPair(left, mid)
        rightPair, rightClosest, = ClosestPair(right, n - mid)

        # select the closest between the left and right subdivision
        if leftClosest < rightClosest:
            closest = leftClosest
            pointsPair = leftPair
        elif leftClosest > rightClosest:
            closest = rightClosest
            rightLen = rightPair.size
            pointsPair = mid + rightPair[0:rightLen]
        else:
            closest = leftClosest
            rightLen = rightPair.size
            pointsPair = numpy.append(leftPair, mid + rightPair[0:rightLen])
        # case 2 : diff side
    return (pointsPair, numpy.round(closest, 2))
    

