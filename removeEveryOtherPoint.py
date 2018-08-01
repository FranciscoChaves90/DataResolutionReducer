# Author:       Francisco Chaves
# Date:         01.August.2018
# Description:  Reduces the number of points in a data set based on a set distance

# Things to do:
#       Comment, Organize Code, User Input Section

import numpy as np
import os
import math

# Define maximum distance threshold
threshold = 20 #metres

# Read file and store data in a numpy array
data = np.genfromtxt('South Quay 5m x 5m grid @ LAT.xyz',skip_header=16)
# Calculate the number of lines and columns of the data array
noLines = data.shape[0]
noColumns = data.shape[1]

# Initiate variables and flags
distanceVector = []
k = 0
completionTracker = 1
tooCloseFlag = 0

#
while completionTracker == 1:
    for i in range(noLines):
        distanceVector.extend([(math.sqrt((data[k][0]-data[i][0])**2+(data[k][1]-data[i][1])**2))])
    # Get index of points closer than X metres
    distanceVectorArray     = np.array(distanceVector)
    closerThanThreshold     = np.where(distanceVectorArray<threshold)[0]
    sortedCloserThanThreshold = sorted(closerThanThreshold[0:],reverse=True)
    sortedCloserThanThresholdArray = np.array(sortedCloserThanThreshold)
    for i in range(sortedCloserThanThresholdArray.shape[0]-1):
            data = np.delete(data,sortedCloserThanThreshold[i],0)
    noLines = data.shape[0]
    noColumns = data.shape[1]
    for i in range(noLines):
        for j in range(0,noLines):
            distance = math.sqrt((data[j][0]-data[i][0])**2+(data[j][1]-data[i][1])**2)
            if distance < threshold and distance != 0:
                print distance
                print [i,j]
                tooCloseFlag = 1
                k = i
                break
        if tooCloseFlag == 1:
            break
    if tooCloseFlag == 0:
        completionTracker=0
    del distanceVector,distanceVectorArray,closerThanThreshold,sortedCloserThanThreshold,sortedCloserThanThresholdArray
    distanceVector = []
    tooCloseFlag = 0
    print data.shape

fid = open('ReducedData.xyz','w')

for i in range(data.shape[0]):
    fid.write('%.3f,%.3f,%.3f\n' % (data[i,0],data[i,1],data[i,2]))
fid.close()
