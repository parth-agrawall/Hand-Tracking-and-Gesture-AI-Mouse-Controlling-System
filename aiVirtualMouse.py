import cv2
import mediapipe as mp
import time
import pyautogui
import numpy as np
import HandTrackingModule as htm

wCam , hCam  = 640,480
frameR = 100 #Frame Reduction

cTime = 0
pTime = 0
smoothening = 7
clocX , clocY = 0,0
plocX, plocY = 0,0

cap = cv2.VideoCapture(0)
cap.set(3,wCam) #propID and width
cap.set(4,hCam) #propID and height

detector = htm.handDetector(maxHands=1)

wScr , hScr = pyautogui.size()  # to get height and width of the respective screen 

while True:
    success, img = cap.read()
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # print(bbox)

    # ------------------------checking coordinates of fingers----------------------------------------------------
    if len(lmList) !=0:
        x1 , y1 = lmList[8][1:] #for index finger 
        x2 , y2 = lmList[12][1:] #for middle finger
        # print(x1, y1, x2, y2)
    #------------------------------------------------------------------------------------------------

    
        fingers = detector.fingersUp() 
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),(255,0,255),2)
        # print(fingers)
        if fingers[1] == 1 and fingers[2] == 0 :   # checking which finger is up

            #------------------converting coordinates------------------
            x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3 = np.interp(y1,(0,hCam-frameR),(0,hScr))
            clocX = plocX + (x3-clocX) / smoothening
            clocY = plocY + (y3-clocY) / smoothening
            #----------------------------------------------------------

            pyautogui.moveTo(wScr - clocX , clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)

            plocX,plocY = clocX,clocY

            # x4 = np.interp(x2,(0,wCam),(0,wScr))
            # y4 = np.interp(y2,(0,hCam),(0,hScr))

            #-------------------------------- Click Detection --------------------------------
        #---------------------- Detect Distance --------------------------------
        if fingers[1] == 1 and fingers[2] == 1:
            length,img,lineInfo = detector.findDistance(8,12,img)
            # print(length)
            # -------------- Click --------------
            if length<40:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                pyautogui.click()

    cv2.putText(img,str(int(fps)), (20,50),cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0),3)
    cv2.imshow("Virtual Mouse",img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
