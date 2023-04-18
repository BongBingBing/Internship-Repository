from cProfile import label
from turtle import color
import numpy as np
import swift
import roboticstoolbox as rtb
from spatialmath import *
from spatialmath import SE3,  Twist3
import time 

#assigning the robot to be used as the UR5 robot

robot = rtb.models.Panda()

#enabling simulation evnironment as well as adding the robot to the environment

env = swift.Swift()
env.launch(realtime = True)
env.add(robot)

#importing a text file for the X, Y, and Z values to be plotted

A = np.loadtxt("")

#creating a loop to run through every point in the text file

i = 0
n = 0

while (n!=10): #change the value here to the amount points on the txt file
    
    #seperating the values on the text file to X, Y, and Z
    
    Xcord = A[0][i]
    Ycord = A[1][i]
    Zcord = A[2][i]
    
    n += 1
    i += 1
    
    #using the X, Y, and Z coords, we use spatial math to create solvable trajectory paths
    
    Tep = SE3.Trans(Xcord, Ycord, Zcord) * SE3.OA([0 ,1 ,0], [0,0,-1]) 
    
    #using lm_chan solver, we solve for the trajectory we desire
    
    sol = robot.ik_lm_chan(Tep)
    
    #set the desired solution to the end position of the robot
    
    q_pickup = sol[0]
    
    #creating a trajectory from the assigned start and end position
    
    qt = rtb.jtraj(robot.qr, q_pickup, 50)
    
    #running through that trajectory as well as adding it to the created environment
    
    for j in range(len(qt)):
        robot.q = qt.q[j,:]
        env.step(0)
        time.sleep(0.05)
    
