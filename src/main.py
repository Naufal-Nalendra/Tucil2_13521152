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
    randomize = input("Use Randomized Points? (Y/N) : ")
    Input, numPoints, dim = Select(randomize)

    distance = 0
    pair = None

    divImpera1 = time.perf_counter()
    # Function to find closest Pair using divide and conquer
    pair, distance = cp.ClosestPair(Input,numPoints)
    divImpera2 = time.perf_counter()
    # Function to find closest Pair using brute force
    pair2, distance2 = bf.bruteForce(Input)
    bruteForceEnd = time.perf_counter()

    # output variables
    divImperaTime = (divImpera2 - divImpera1)
    bruteForceTime = (bruteForceEnd - divImpera2)

    print('------------------------------------------------------------------')
    print('The closest pair of points are :')
    print(pair[0])
    print(pair[1])
    # print second point
    print('\nWith the distance of :', distance)
    print('And the count of euclidean operations :', cp.euclidCount)
    print('------------------------------------------------------------------')
    # Execution time for DnC and brute force
    print("Divide and Conquer execution time :",divImperaTime * 1000,"ms")
    print("Brute Force execution time :",bruteForceTime * 1000,"ms")
    print('------------------------------------------------------------------')
    # PC specifications
    print("\nMachine Specifications : ")
    print("Processor used : ",platform.processor())
    print("System version : ",platform.platform())
    print("Python version : ",platform.python_version())

    visualize = input("\nDo you want to see the result (y/n) ")
    if (visualize == "y"): 
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
        print('Unable to plot') 

# if __name__ == '__main__':
#     count = 0
#     rand = 1000.0
#     main()
main()