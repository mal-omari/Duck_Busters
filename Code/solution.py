import math
import cv2
import numpy as np

#move_type will always be "absolute"
#current_frame is an image array depicting the current duck hunt environment
#kp1 are the sift keypoints of the duck collage image (query image)
#des1 are the sift descriptors of the duck collage image (query image)
def GetLocation(move_type, current_frame, kp1, des1):
        
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
        
        
        sift = cv2.SIFT_create(); #creates sift object, source: https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html

        frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY) #converts current frame to grayscale
        
        kp2, des2 = sift.detectAndCompute(frame,None) #uses sift to detect the keypoints and descriptors of the frame image, source: https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html

        bf = cv2.BFMatcher() #uses brute force matching object, source: https://docs.opencv.org/3.4/dc/dc3/tutorial_py_matcher.html
        matches = bf.knnMatch(des1,des2,k=2) #finds the matches of the two sift descriptors, source: https://docs.opencv.org/3.4/dc/dc3/tutorial_py_matcher.html

        positions = []  #holds the matching coordinates      
        
        #ratio test to determine the good matches, source: https://docs.opencv.org/3.4/dc/dc3/tutorial_py_matcher.html
        for m,n in matches:
          if m.distance < 0.56*n.distance:
            #gets the coordinates from the train image, current frame, source: https://stackoverflow.com/questions/57859836/how-to-get-key-points-or-pixel-coordinates-of-an-image-from-descriptor-produced
            pos = np.array(kp2[m.trainIdx].pt) 
            pos1 = np.array(kp2[m.trainIdx].pt)  
            pos1[0] = round(pos[1]) #the coordinates are reversed, so need to transpose them
            pos1[1] = round(pos[0])
            positions.append(pos1)  
        
        

        
        if(len(positions)==0): #sends a noop if no matches are found
          coordinate = [-1,-1]
        else:
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
          # Average
          if(len(new_keypoints) == 0):
            coordinate = [-1,-1]
          else:
            coordinate = np.mean(new_keypoints, axis =0)

    return[{'coordinate' : coordinate, 'move_type' : move_type}]
