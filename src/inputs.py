import numpy
import os

def Select(randomize : str):
    if (randomize == "y" or randomize == "Y"):
        random = True
        numPoints = int(input("Enter The Number of Points : "))
        dimension = int(input("Enter The Number of Dimensions : "))
        size = int(input("Enter max threshold size for a point : "))
        points = []
        points = numpy.array(points).astype(float)
        Input = setPoints(numPoints, dimension, size, random, points)
    else:
        random = False
        filename = input("Enter File Name (without file extension) : ")
        path = os.path.realpath(__file__)
        dir = os.path.dirname(path)
        dir = dir.replace('src', 'input')
        os.chdir(dir)
        points = []
        with open(f"{dir}\\{filename}.txt", 'r') as file:
            for lines in file.read().split('\n'):
                print(lines.split(' '))
                points.append(lines.split(' '))        

        points = numpy.array(points).astype(float)
        numPoints = len(points)
        dimension = len(points[0])
        size = numpy.max(points)

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
    array = numpy.round(array,2)
    array = numpy.sort(array, axis=0)
    return array

def randomPoints(num : int, dim : int, max : int, array):
    print("Points are randomized")
    
    vector = []
    for i in range(num * dim):
        a = numpy.random.uniform(low=0.0, high = max)
        vector.append(a)
    array = numpy.array(vector).reshape(num, dim)
    return array