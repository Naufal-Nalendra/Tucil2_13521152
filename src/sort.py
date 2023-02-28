import numpy

def quickSort(points: numpy.array, dimension: int, lowerIdx: int, upperIdx: int):
    if lowerIdx < upperIdx:
        # First partition to search for pivot
        index = Partition(points, dimension, lowerIdx, upperIdx)
        # Apply recursion for the left and right side of pivot
        quickSort(points, dimension, lowerIdx, index - 1)
        quickSort(points, dimension, index + 1, upperIdx)
        
def Partition(points: numpy.array, dimension : int, lowerIdx: int, upperIdx: int):
    # Choose first column of last row as pivot
    pivot = points[upperIdx][0]

    # Count the number of pass
    passed = lowerIdx - 1

    # Compare points value with pivot
    for j in range(lowerIdx, upperIdx):
        # Swap if lower than pivot
        if points[j][0] <= pivot:
            passed += 1
            for col in range(dimension):
                temp = points[j][col]
                points[j][col] = points[passed][col]
                points[passed][col] = temp

    # Swap with pivot
    for p in range(dimension):
        temp = points[upperIdx][p]
        points[upperIdx][p] = points[passed+1][p]
        points[passed+1][p] = temp
    
    # Return index for the next sort
    return (passed+1)


