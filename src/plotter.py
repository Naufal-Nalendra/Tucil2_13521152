import matplotlib.pyplot as plt
import numpy

def plot2d(pointArr: numpy.array, pairOfPoints : numpy.array, filename : str):
    print('------------------------------------------------------------------')
    print("Please wait a moment..")
    # Create arrays for points and result points
    xres = []
    yres = []
    x = []
    y = []

    # Insert points into respective arrays
    numPoints = pointArr.shape[0]
    for i in range(numPoints):
        if i not in pairOfPoints:
            x.append(pointArr[i,0])
            y.append(pointArr[i,1])
        else:
            xres.append(pointArr[i,0])    
            yres.append(pointArr[i,1])       

    plt.scatter(x, y, color= "black", linewidth=0.5)
    plt.scatter(xres, yres, color="orange", linewidth=1.0)
    plt.savefig('images/' + filename + '.png') 

    plt.show()
    
def plot3d(pointArr: numpy.array, pairOfPoints : numpy.array, filename : str):
    print('------------------------------------------------------------------')
    print("Please wait a moment..")

    fig = plt.figure()
    axis = plt.axes(projection='3d')

    # Create arrays for points and result points
    xres = []
    yres = []
    zres = []
    x = []
    y = []
    z = []

    # Insert points into respective arrays
    numPoints = pointArr.shape[0]
    for i in range(numPoints):
        if i not in pairOfPoints:
            x.append(pointArr[i,0])
            y.append(pointArr[i,1])
            z.append(pointArr[i,2])
        else:
            xres.append(pointArr[i,0])    
            yres.append(pointArr[i,1])    
            zres.append(pointArr[i,2])   
            
    # Labeling the axis
    axis.set_xlabel('X axis')
    axis.set_ylabel('Y axis')
    axis.set_zlabel('Z axis')

    axis.scatter(x, y, z, s = 60 ,color= "black", linewidth=0.5)
    axis.scatter(xres, yres, zres, s = 80 ,color="red", linewidth=2.0)
    plt.savefig('images/' + filename + '.png') 

    plt.show()