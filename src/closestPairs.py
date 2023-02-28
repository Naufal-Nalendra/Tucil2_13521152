import numpy

euclidCount = 0

def euclideanDistance(arr1 : numpy.array, arr2 : numpy.array):
    global euclidCount
    euclidCount += 1
    
    squared = numpy.square(arr1 - arr2)
    squared_sum = numpy.sum(squared)
 
    return numpy.sqrt(squared_sum)

def ClosestPair(points : numpy.array, numPoints : int):
    closest = float('inf')
    pointsPair = numpy.array([])
    if (numPoints == 1):
        print("There is no answer")
    elif (numPoints == 2):
        closest = euclideanDistance(points[0], points[1])
        pointsPair = numpy.array([0, 1])
    elif (numPoints == 3):
        closest = euclideanDistance(points[1], points[2])
        pointsPair = numpy.array([1, 2])
        for i in range(0, 3):
            if (i != 0):
                temp = euclideanDistance(points[0], points[i])
                if temp < closest:
                    pointsPair = numpy.array([0, i])
                    closest = temp
    else:
        # case 1 : same side
        mid = int(numPoints/2)
        left = points[0:mid]
        right = points[mid:numPoints]

        # split into left and right
        leftPair, leftClosest, = ClosestPair(left, mid)
        rightPair, rightClosest, = ClosestPair(right, numPoints - mid)

        # select the closest between the left and right subdivision
        if leftClosest < rightClosest:
            closest = leftClosest
            pointsPair = leftPair
        elif leftClosest > rightClosest:
            closest = rightClosest
            pointsPair = mid + rightPair[0:rightPair.size]
        else:
            closest = leftClosest
            pointsPair = numpy.append(leftPair, mid + rightPair[0:rightPair.size])
        # case 2 : diff side
        midPoint = (points[mid - 1][0] + points[mid][0]) / 2
        midPoints = []
        for i in range(numPoints):
            if abs(points[i][0] - midPoint) < closest:
                midPoints.append(points[i])

        # compare each point in the strip with its 7 neighbors (if they exist)
        for i in range(len(midPoints)):
            for j in range(i + 1, min(i + 8, len(midPoints))):
                found = True
                for k in range(len(midPoints[i])):
                    if abs(midPoints[i][k] - midPoints[j][k]) > closest:
                        found = False
                if(found):
                    distance = euclideanDistance(midPoints[i], midPoints[j])
                    if distance < closest:
                        closest = distance
                        id1 = numpy.where((points == midPoints[i]).all(axis=1))[0][0]
                        id2 = numpy.where((points == midPoints[j]).all(axis=1))[0][0]
                        pointsPair = numpy.array([points[id1],points[id2]])
                        
    return (pointsPair, numpy.round(closest, 3))
