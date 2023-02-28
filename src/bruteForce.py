import math
import numpy as np
from closestPairs import euclideanDistance

count= 0

def bruteForce(points : np.array):
    global count
    closest = math.inf
    closestPair = None

    # Iterate over all pairs of points
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            # Calculate the Euclidean distance
            distance = euclideanDistance(points[i], points[j])
            count += 1
            # Check for the closest pair
            if distance < closest:
                closest = distance
                closestPair = (points[i], points[j])

    return closestPair, closest
