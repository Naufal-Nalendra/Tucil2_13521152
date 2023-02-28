import numpy
import os
from sort import quickSort

def validate(prompt, criteria):
    while True:
        try:
            userInput = input(prompt)
            if criteria(userInput):
                return userInput
            else:
                print("Invalid input. Please try again.")
                print('------------------------------------------------------------------')
        except ValueError:
            print("Invalid input. Please try again.")
            print('------------------------------------------------------------------')

def generatePoints():
    random = True

    numPoints = int(validate("\nEnter the number of points: ", lambda x: int(x) > 0))
    dimension = int(validate("Enter the number of dimensions: ", lambda x: int(x) > 0))
    size = int(validate("Enter the max range of a point: ", lambda x: int(x) > 0))

    points = []
    points = numpy.array(points).astype(float)
    Input = setPoints(numPoints, dimension, size, random, points)
        
    return Input

def setPoints(n_points : int, n_dim : int, size : int, random : bool, inputPoints):
    num = n_points
    dim = n_dim
    max = size
    array = []
    array = numpy.array(array).astype(float)

    if(random == True):
        array = randomPoints(num,dim,max,array)
    else:
        array = inputPoints
    array = numpy.round(array,3)
    
    # sort array
    quickSort(array, dim, 0, num-1)
    return array, num, dim

def randomPoints(num : int, dim : int, max : int, array):
    print('------------------------------------------------------------------')
    print("Points are randomized")
    
    vector = []
    for i in range(num * dim):
        a = numpy.random.uniform(low=0.0, high = max)
        vector.append(a)
    array = numpy.array(vector).reshape(num, dim)
    return array