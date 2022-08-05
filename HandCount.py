import cv2 as cv
import time
import os
import HandTrackingModule as htm


pTime =0

wCam,hCam=640,480
cap=cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

detector=htm.handDetector(detectionCon=0.75)
tips=[4,8,12,16,20]


count=0
bol =False
while True :
    success,img=cap.read()
    img=detector.findHands(img)
    landmark=detector.findPosition(img,draw=False )
    #print(landmark)
    if len(landmark)!=0:
        fingers=[]
        if landmark[tips[0]][1] < landmark[tips[0] - 1][1]:
            fingers.append(1)
        else :
            fingers.append(0)
        for id in range (1,5):

            if landmark[tips[id]][2]<landmark[tips[id]-2 ][2]:
                  fingers.append(1)
            else :
                fingers.append(0)
        count=fingers.count(1)
        cv.putText(img,str(count),(120,300),cv.FONT_HERSHEY_SIMPLEX,2,(255,0,0),4)

        print(fingers)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv.putText(img,str(count),(320,70),cv.FONT_ITALIC,3,(255,9,240),3)

    cv.putText(img,str(int(fps)),(20,79),cv.FONT_ITALIC,3,(255,9,240),3)

    cv.imshow("img", img)

    cv.waitKey(1)

