from matplotlib import pyplot as plt
def GetLocation(move_type, env, current_frame):
    time.sleep(1) #artificial one second processing time
    
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
        coordinate = env.action_space.sample() 
    #Use absolute coordinates for the position of the "gun", coordinate space are defined below
    else:
        """
        (x,y) coordinates
        Upper left = (0,0)
        Bottom right = (W, H) 
        """
        #note, couldn't get the wget to work so just uploaded it manually
        duck = cv2.cvtColor(cv2.imread('Level_1.png'),cv2.COLOR_RGB2GRAY)
        sift = cv2.SIFT_create();

        frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        kp1, des1 = sift.detectAndCompute(duck,None)
        kp2, des2 = sift.detectAndCompute(frame,None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)

        indexes = []
        
        
        for m,n in matches:
          if m.distance < 0.9*n.distance:
            indexes.append(m.trainIdx)
            
        print("num match", len(indexes))

        positions = []
        for ip in range(len(indexes)):
          
          pos = np.array(kp2[ip].pt)
          pos1 = np.array(kp2[ip].pt)
          if(int(pos[1]) !=641 and pos[1] > 20):
            pos1[0] = pos[1]
            pos1[1] = pos[0]
            positions.append(pos1)
        

        
        if(len(positions)==0):
          coordinate = [0,0]
        else:
          coordinate = positions[0]
        print(coordinate)
        
    
    return [{'coordinate' : coordinate, 'move_type' : move_type}]
