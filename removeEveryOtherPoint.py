# Author:       Francisco Chaves
# Date:         01.August.2018
# Description:  Reduces the number of points in a data set based on a set distance

# Import required libraries
import numpy as np
import os
import math

# User input
threshold       = 20                 # Minimum desired distance between points
inputFilename   = 'OriginalData.xyz' # Name of input file
headerLines     = 16                 # Number of header lines on input file
outputFilename  = 'ReducedData.xyz'  # Name of output file

# Read file and store data in a numpy array
data = np.genfromtxt(inputFilename,skip_header=16)
# Calculate the number of lines and columns of the data array
noLines   = data.shape[0]
noColumns = data.shape[1]
print "Original number of points in the file: %d\n" % noLines

# Initiate variables and flags
distanceVector = []
k = 0
completionTracker = 1
tooCloseFlag = 0
iterationCounter = 0

# Main data removal loop
while completionTracker == 1:
    # Keep track on number of loops (only for printing purposes)
    iterationCounter +=1
    # Calculate the distance from point k to all other points
    for i in range(noLines):
        distanceVector.extend([(math.sqrt((data[k][0]-data[i][0])**2+(data[k][1]-data[i][1])**2))])
    # Convert distanceVector (list) to a numpy array (to allow the use of numpy's functions)
    distanceVectorArray     = np.array(distanceVector)
    # Find which elements in distanceVectorArray are lower than the defined threshold
    # This command provides a list of indices that satisfy the criteria
    closerThanThreshold     = np.where(distanceVectorArray<threshold)[0]
    # Sort the closerThanThreshold list in reverse order (that later we remove points from bottom to top)
    sortedCloserThanThreshold = sorted(closerThanThreshold[0:],reverse=True)
    # Convert the list into a numpy array
    sortedCloserThanThresholdArray = np.array(sortedCloserThanThreshold)
    # Remove the elements (from bottom to top) which were identified as being closer than the threshold
    for i in range(sortedCloserThanThresholdArray.shape[0]-1):
            data = np.delete(data,sortedCloserThanThreshold[i],0)
    # Re-calculate the number of lines of the new data array (points have already been removed)
    oldNoLines  = noLines # Only for printing purposes
    noLines     = data.shape[0]
    noColumns   = data.shape[1]
    print "Sweep %d...\nNumber of points removed > %d points <\nTotal number of points > %d points <\n" % (iterationCounter,oldNoLines-noLines,noLines)
    # loop to identify if there are points closer to each other of a distance below the specified closerThanThreshold
    # Loop through each point
    for i in range(noLines):
        # Calculate the distance between each point to all other points
        for j in range(0,noLines):
            distance = math.sqrt((data[j][0]-data[i][0])**2+(data[j][1]-data[i][1])**2)
            # As soon as a pair of points is found closer than the specified distance, we break the loop
            if distance < threshold and distance != 0:
                # Raise a flag identifying that a set of points too close to each other was found
                tooCloseFlag = 1
                # The next point to analyse in the main loop is "idea"
                k = i
                break
        # Once the tooCloseFlag is raised, break out of the "distance checking loop"
        if tooCloseFlag == 1:
            break
    # If no points are found too close to each other, raise the completionTracker flag (to indentify that the task is complete and break out of the while loop)
    if tooCloseFlag == 0:
        completionTracker=0
        print "Point removal complete.\n"
    # Clear variables (still uncertain as to how re-writting variables works in python, deleting for safety)
    del distanceVector,distanceVectorArray,closerThanThreshold,sortedCloserThanThreshold,sortedCloserThanThresholdArray
    distanceVector = []
    # Re-set the tooCloseFlag to 0
    tooCloseFlag = 0

# Write the new data file to an .xyz file.
fid = open(outputFilename,'w')
for i in range(data.shape[0]):
    fid.write('%.3f,%.3f,%.3f\n' % (data[i,0],data[i,1],data[i,2]))
fid.close()
print ">> Task complete sucessfully <<"
