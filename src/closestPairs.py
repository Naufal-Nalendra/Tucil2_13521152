import numpy

euclidCount = 0

def euclideanDistance(arr1 : numpy.array, arr2 : numpy.array):
    global euclidCount
    euclidCount += 1
    
    squared = numpy.square(arr1 - arr2)
    squared_sum = numpy.sum(squared)
 
    return numpy.sqrt(squared_sum)

# def ClosestPair(vectors : numpy.array, n : int):
#     closest : float
#     idxpair = numpy.array([])
#     if (n == 1):
#         print("No Closest Pair for one point!")
#     elif (n == 2):
#         # print("Pair")
#         closest = euclideanDistance(vectors[0], vectors[1])
#         idxpair = numpy.array([0, 1])
#     elif (n == 3):
#         # print("Triplet")
#         closest = euclideanDistance(vectors[1], vectors[2])
#         idxpair = numpy.array([1, 2])
#         for i in range(0, 3):
#             if (i != 0):
#                 temp = euclideanDistance(vectors[0], vectors[i])
#                 if temp < closest:
#                     idxpair = numpy.array([0, i])
#                     closest = temp
#     else:
#         # case 1 : smallest pair is in the same side
#         # divide the array
#         n_div = int(n / 2)
#         # print("ndiv:", n_div)

#         left = vectors[0:n_div]
#         right = vectors[n_div:n]

#         # print(left)
#         # print(right)
#         # print(n_div, n)

#         # split into left and right
#         leftidxpair, leftclosest = ClosestPair(left, n_div)
#         rightidxpair, rightclosest = ClosestPair(right, n - n_div)

#         # select the closest between the left and right subdivision
#         if leftclosest < rightclosest:
#             closest = leftclosest
#             idxpair = leftidxpair
#         elif rightclosest < leftclosest:
#             closest = rightclosest
#             idxpair = rightidxpair[0:rightidxpair.size] + n_div
#         else:
#             closest = leftclosest # or right, it's the same
#             idxpair = numpy.append(leftidxpair, rightidxpair[0:rightidxpair.size] + n_div)

#         # case 2 : smallest pair is on a separate subdivision
#         # use closest as delta
#         # x0 is the middle point of division
#         x0 = ((vectors[n_div-1][0] + vectors[n_div][0]) / 2)
#         # get all points inside the slab x0 with unbounded y and z
#         allpoints = numpy.array([])
#         idxmapping = numpy.array([])
#         npoints = 0
#         for i in range(n):
#             if vectors[i][0] >= x0 - closest and vectors[i][0] <= x0 + closest:
#                 allpoints = numpy.append(allpoints, vectors[i])
#                 idxmapping = numpy.append(idxmapping, i)
#                 npoints += 1
#         allpoints = numpy.reshape(allpoints, (npoints, vectors[0].size))

#         nrow, ncol = allpoints.shape
#         for i in range(0, nrow):
#             for j in range(0, nrow):
#                 if i != j:
#                     p1 = allpoints[i]
#                     p2 = allpoints[j]
#                     # get all distance of p1 and p2 in the y and z dimension (in n-dimension, get all n-1 dimension's distance)
#                     p3 = abs(p1 - p2)[1:]
#                     # check if their distances <= delta (closest)
#                     # this is the constraint (sparsity condition)
#                     if all(x <= closest for x in p3):
#                         distance = euclideanDistance(p1, p2)
#                         if distance < closest:
#                             closest = distance
#                             idxpair = numpy.array([idxmapping[i], idxmapping[j]]).astype(int)
#                             # print(idxpair, idxpair[0])
        
#     # Calculating the T(n) : O(n log n) (from the DnC algorithm) + O(nk) (see the above comments for description) = O(n log n)
#     return idxpair, numpy.round(closest, 3)

def ClosestPair(points : numpy.array, n : int):
    closest = 0.0
    pointsPair = numpy.array([])
    if (n == 1):
        print("No Closest Pair for one point!")
    elif (n == 2):
        # print("Pair")
        closest = euclideanDistance(points[0], points[1])
        pointsPair = numpy.array([0, 1])
    elif (n == 3):
        # print("Triplet")
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
            pointsPair = mid + rightPair[0:rightPair.size]
        else:
            closest = leftClosest
            pointsPair = numpy.append(leftPair, mid + rightPair[0:rightPair.size])
        # case 2 : diff side
        midPoint = (points[mid - 1][0] + points[mid][0]) / 2
        midPoints = []
        for i in range(n):
            if abs(points[i][0] - midPoint) < closest:
                midPoints.append(points[i])

        # sort the strip points by their y-coordinate
        midPoints.sort(key=lambda x: x[1])

        # compare each point in the strip with its 7 neighbors (if they exist)
        for i in range(len(midPoints)):
            for j in range(i + 1, min(i + 8, len(midPoints))):
                found = True
                for k in range(len(midPoints[i])):
                    if abs(midPoints[i][k] - midPoints[j][k]) > closest:
                        found = False
                distance = euclideanDistance(midPoints[i], midPoints[j])
                if distance < closest:
                    closest = distance
                    pointsPair = numpy.array([midPoints[i], midPoints[j]])
    return (pointsPair, numpy.round(closest, 3))