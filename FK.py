from cProfile import label
from turtle import color
import numpy as np
import swift
import roboticstoolbox as rtb
from spatialmath import *
from spatialmath import SE3,  Twist3
import spatialmath as sm
import spatialgeometry as sg
import time 

#assigning the robot to be used as the UR5 robot

robot = rtb.models.Panda()

#enabling simulation evnironment as well as adding the robot to the environment

env = swift.Swift()
env.launch(realtime = True)
env.add(robot)

#creating an array of present joint angles for the robot to follow (notice 6 joints on the robot so 6 arrays)

joint = [[-0.1, -0.2, -0.3, -0.4, -0.5],
         [-0.1, -0.2, -0.3, -0.4, -0.5],
         [-0.1, -0.2, -0.3, -0.4, -0.5],
         [-0.1, -0.2, -0.3, -0.4, -0.5],
         [-0.1, -0.2, -0.3, -0.4, -0.5],
         [-0.1, -0.2, -0.3, -0.4, -0.5]]

#creating a while loop to run through every joint angle in the array

i = 0
n = 0

while (n!=5):

    #end-point joint angles
    
    j0 = joint[0][i]
    j1 = joint[1][i]
    j2 = joint[2][i]
    j3 = joint[3][i]
    j4 = joint[4][i]
    j5 = joint[5][i]

    #starting-point joint angles

    p0 = joint[0][i-1]
    p1 = joint[1][i-1]
    p2 = joint[2][i-1]
    p3 = joint[3][i-1]
    p4 = joint[4][i-1]
    p5 = joint[5][i-1]
    
    i += 1
    n += 1
    
    #assigning the end and start joint positions of the robot as a whole
    
    q_pickup = np.array([j0, j1, j2, j3, j4, j5])
    robot.qr = np.array([p0, p1, p2, p3, p4, p5])
    
    #creating a trajectory using the start and end joint positions
    
    qt = rtb.jtraj(robot.qr, q_pickup, 50)

    #running through that trajectory as well as adding it to the created environment

    for j in range(len(qt)):
        robot.q = qt.q[j,:]
        env.step(0)
        time.sleep(0.05)
