import cv2
import mediapipe as mp
import time
import math
cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils # to draw lines



class handDetector():
    def __init__(self, mode = False, maxHands = 2, modelComplexity = 1, detectionCon = 0.5, trackingCon = 0.5):
                self.mode = mode
                self.maxHands = maxHands
                self.modelComplexity = modelComplexity
                self.detectionCon = detectionCon
                self.trackingCon = trackingCon

                self.mpHands = mp.solutions.hands
                self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComplexity,self.detectionCon,self.trackingCon)
                self.mpDraw = mp.solutions.drawing_utils
                self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self,img, draw = True):
                

        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # as hands uses RGB images
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks: #if hand landmark is detected then:
            for handLms in self.results.multi_hand_landmarks: 
                    if draw:
                        self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self,img,handNo=0,draw=True):
        xList = []
        yList = []
        self.lmList = [] #will return all landmark positions
        bbox = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo] 
            for id,lm in enumerate(myHand.landmark):
                h , w , c = img.shape #height, width and channel
                cx,cy = int(lm.x*w),int(lm.y * h) #centre of landmarks

                xList.append(cx)
                yList.append(cy)

                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy),5,(255,0,255), cv2.FILLED)
                
            xMin, xMax = min(xList),max(xList)
            yMin, yMax = min(yList),max(yList)
            bbox = xMin , yMin, xMax, yMax

            if draw:
                cv2.rectangle(img, (xMin - 20, yMin - 20), (xMax + 20, yMax + 20),(0, 255, 0), 2)
                # print(id,lm)
        return self.lmList,bbox
    
    def fingersUp(self):
        fingers = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers
        for id in range(1, 5):

            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # totalFingers = fingers.count(1)

        return fingers
    
    def findDistance(self, p1, p2, img, draw=True,r=15, t=3):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2, cx, cy]

def main():

    pTime = 0 
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist   = detector.findPosition(img)

        if len(lmlist)!=0: #only if hand and that particular index is detected then only print
            print(lmlist[4])
        cTime = time.time() #current time
        fps = 1/(cTime-pTime) #fps
        pTime = cTime #previous time

        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

        cv2.imshow("Image",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()