import time
import numpy as np
import platform
from inputs import *
import plotter as pt
import closestPairs as cp
import bruteForce as bf

def main():
    global count
    global rand
    global euclidCount
    # Open the text file in read mode
    with open('src/splashScreen.txt', 'r') as file:
        contents = file.read()
        print(contents)
    
    # Function to validate inputs
    Input, numPoints, dim = generatePoints()

    distance = 0
    pair = None

    divImpera1 = time.perf_counter()
    # Function to find closest Pair using divide and conquer
    pair, distance = cp.ClosestPair(Input,numPoints)
    dnc = cp.euclidCount
    divImpera2 = time.perf_counter()
    # Function to find closest Pair using brute force
    pairbf, distancebf = bf.bruteForce(Input)
    bfdistance = numpy.round(distancebf, 3)
    bfCount = bf.count
    bruteForceEnd = time.perf_counter()

    # output variables
    divImperaTime = numpy.round(divImpera2 - divImpera1, 8)
    bruteForceTime = numpy.round(bruteForceEnd - divImpera2, 8)
    # Divide and Conquer Algorithm
    print('------------------------------------------------------------------')
    print('DIVIDE AND CONQUER')
    print('------------------------------------------------------------------')
    print('The closest pair of points are :')
    print(pair[0])
    print(pair[1])
    # print second point
    print('\nWith the distance of :', distance)
    print('And the count of euclidean operations in DnC :', dnc)
    print("Divide and Conquer execution time :",divImperaTime * 1000,"ms")
    # Brute Force Algorithm
    print('------------------------------------------------------------------')
    print('BRUTE FORCE')
    print('------------------------------------------------------------------')
    print('The closest pair of points are :')
    print(pairbf[0])
    print(pairbf[1])
    # print second point
    print('\nWith the distance of :', bfdistance)
    print('And the count of euclidean operations in Brute Force :', bfCount)
    print("Brute Force execution time :",bruteForceTime * 1000,"ms")
    print('------------------------------------------------------------------')
    # PC specifications
    print("\nMachine Specifications : ")
    print("Processor used : ",platform.processor())
    print("System version : ",platform.platform())
    print("Python version : ",platform.python_version())

    visualize = input("\nDo you want to see the plot? (Y/N) ")
    if (visualize == "y" or visualize == "Y"): 
        print('------------------------------------------------------------------')
        print("The result will be saved in the folder 'images'")
        name = input("Please enter the desired file name :")
        if(dim == 2):
            pt.plot2d(Input, pair, name)
        elif(dim == 3):
            pt.plot3d(Input, pair, name)
        else:
            print(dim, 'th', 'dimension cannot be plotted')
    else:
        print('Thank you for using our program :) ') 
        
# run main
main()