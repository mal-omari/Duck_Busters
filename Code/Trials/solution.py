import time
import math
import cv2
import numpy as np

def GetLocation(move_type, current_frame):
    #time.sleep(1) #artificial one second processing time
    
    #Use relative coordinates to the current position of the "gun", defined as an integer below
    if move_type == "relative":
        """
        North = 0
        North-East = 1
        East = 2
        South-East = 3
        South = 4
        South-West = 5
        West = 6
        North-West = 7
        NOOP = 8
        """
        coordinate = action_space.sample()  
    #Use absolute coordinates for the position of the "gun", coordinate space are defined below
    else:
        """
        (x,y) coordinates
        Upper left = (0,0)
        Bottom right = (W, H) 
        """
        
        duck = cv2.cvtColor(cv2.imread('DuckAll.png'),cv2.COLOR_RGB2GRAY)
        sift = cv2.SIFT_create();

        frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        kp1, des1 = sift.detectAndCompute(duck,None)
        kp2, des2 = sift.detectAndCompute(frame,None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)

        positions = []        
        cv2.imwrite("frame.png", frame)
        for m,n in matches:
          if m.distance < 0.56*n.distance:
            pos = np.array(kp2[m.trainIdx].pt)
            pos1 = np.array(kp2[m.trainIdx].pt)  
            pos1[0] = round(pos[1])
            pos1[1] = round(pos[0])
            positions.append(pos1)  
        #print("num match", len(positions))
        possy = np.expand_dims(np.array(positions),axis=0)

        
        if(len(positions)==0):
          coordinate = [-1,-1]
        else:
          #coordinate = np.mean(positions, axis = 0)

          keypoints = []
          keypoints = positions.copy()
          # Find centroid
          centroid = np.mean(keypoints, axis = 0)
          # Compute the Euclidean distance of all points to the centroid
          EuclideanDistance = []
          for i in range(0, len(keypoints)):
            point = keypoints[i]
            a = point[0] - centroid[0]
            b = point[1] - centroid[1]
            distance = math.sqrt((a**2) + (b**2))
            EuclideanDistance.append(distance)
          EuclideanDistance = np.array(EuclideanDistance)
          mean, std = cv2.meanStdDev(EuclideanDistance)
          mean = mean[0][0]
          std = std[0][0]
          new_keypoints = []
          # Filter original keypoints
          for ip in range(0, len(positions)):
            if EuclideanDistance[ip] <= mean + 2.1*std:
              new_keypoints.append(keypoints[ip])
          
          if(len(new_keypoints) == 0):
            coordinate = [-1,-1]
          else:
            coordinate = np.mean(new_keypoints, axis =0)

    return[{'coordinate' : coordinate, 'move_type' : move_type}]
