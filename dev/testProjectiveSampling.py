#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:27:09 2019

@author: jasper

Load the sample data  frame and run this on it
"""

"""
Applies the projective equations to the depth map to calculate where the physical sensor would
read a pixel from, then returns a boolean mask with a 1 in this position and zeros elsewhere.
"""

F = 518.86; #The focal length of the camera in pixels (value in NYU toolbox is 518.86 @ 640x480)
X = -26.75; #The X offset of the ToF from camera in mm (default -26.75mm)
Y = 26.81; #The Y offset of the ToF from camera in mm (default 26.81mm)

#Correct for resized image
F = F*(depth.shape[1]/640)

Ox = depth.shape[1]/2
Oy = depth.shape[0]/2

maxDepth = int(np.amax(depth)*1000)
depthInc = int(10) #1cm increments

for testDepth in range(depthInc, maxDepth, depthInc):
    #For each possible depth, check if the projection of ToF at that depth is greater than the measured depth
    u = F*X/testDepth + Ox
    v = F*Y/testDepth + Oy

    if((u > 2*Ox) or (v > 2*Oy)):
        continue

    u = int(u)
    v = int(v)
    
    measuredDepth = 1000*depth[v,u]
    
    #Skip unfilled depth values        
    if(measuredDepth < depthInc):
        continue
    
    if(measuredDepth < testDepth):
        mask = np.zeros((depth.shape), dtype=bool)
        mask[v,u] = True
        break;
        print("return mask");


print("ERROR: Reached Max Projection Depth")
print("return 0");