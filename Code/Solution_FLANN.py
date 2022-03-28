import time
import cv2
import numpy as np

def GetLocation(move_type, env, current_frame):
    #time.sleep(1) #artificial one seconf processing time

    #Use relative coordinates to the current position of the "Gun", defind as an integer below
    if move_type == "relative":
        coordinate = env.action_space.sample()

    else:
        duck = cv2.cvtColor(cv2.imread('/home/farouq/Desktop/ECE471/ece471_536-S2022/duck-hunt/ducks.png'),cv2.COLOR_RGB2GRAY)
        
        sift = cv2.xfeatures2d.SIFT_create()

        frame = cv2.resize(cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY), None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
        kp1, des1 = sift.detectAndCompute(duck,None)
        kp2, des2 = sift.detectAndCompute(frame,None)

        FLAN_INDEX_KDTREE = 0
        index_params = dict (algorithm = FLAN_INDEX_KDTREE, trees=5)
        search_params = dict (checks=50)
        
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch (des1, des2,k=2)

        positions = []
        #cv2.imwrite("frame.png", frame)

        for m1, m2 in matches:
            if m1.distance < 0.5 * m2.distance:
                pos = np.array(kp2[m1.trainIdx].pt)
                pos1 = np.array(kp2[m1.trainIdx].pt)
                pos1[1] = round(pos[0]*2)
                pos1[0] = round(pos[1]*2)
                positions.append(pos1)
            print("Number of Matches: ", len(positions))
        
        #coordinate = np.mean(positions, axis =0)
        #possy = np.expand_dims(np.array(positions),axis=0)

        if(len(positions) == 0):
            coordinate = [0,0]
        else:
            coordinate = positions[-1]
        print(coordinate)

    return[{'coordinate' : coordinate, 'move_type' : move_type}]
