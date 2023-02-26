import math
import numpy as np
from closestPairs import euclideanDistance
from closestPairs import euclidCount

def bruteForce(points : np.array()):
    closest = math.inf
    closestPair = None

    # Iterate over all pairs of points
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            # Calculate the Euclidean distance
            distance = euclideanDistance(points[i], points[j])
            # Check for the closest pair
            if distance < closest:
                closest = distance
                closestPair = (points[i], points[j])

    return closestPair, closest
