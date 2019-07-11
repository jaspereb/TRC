# Author: Jasper Brown
# jasperebrown@gmail.com
# 2019

import numpy as np
"""
Load the sample data  frame and run this on it

Finds the nearest non zero depth pixel to pixx,pixy
"""

#Depth at [y,x]
depth[100:125,150:190] = 0
pixx = 170
pixy = 110


#The index of non zero points
nonZeros = np.nonzero(depth) 

#Distance ordering from [pixx,pixy] to non zero elements
dists = (abs(nonZeros[0]-pixy))**2 + (abs(nonZeros[1]-pixx))**2
minDist = np.argmin(dists)

mask = np.zeros((depth.shape), dtype=bool)
pixy = nonZeros[0][minDist]
pixx = nonZeros[1][minDist]

mask[pixy,pixx] = True