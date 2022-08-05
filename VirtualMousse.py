import cv2 as cv
import numpy as np

import HandTrackingModule as htm
import time
import pyautogui as mousse
from pynput.mouse import Button ,Controller
mouse=Controller()


print(mousse.size())
mousse.FAILSAFE=False


#######
pTime=0

########
cap=cv.VideoCapture(0)





hand=htm.handDetector()


while True :

    success,img=cap.read()
    resized=cv.resize(img,(1920,1080),interpolation=cv.INTER_AREA)

    resized=cv.flip(resized,1)
    img=hand.findHands(resized,draw=False )


    #getting the tip and the index of the midle finger

    #check which of the fingers is up

    #Only index Finger : Moving Mode

        ##Convert Coordinates of screen

    ## Smooth Values
    #
    #Move Mouse
    landmarks=hand.findPosition(resized,draw=False)

    if len(landmarks)!=0:
          x1,y1=landmarks[8][1:]
          x2,y2=landmarks[12][1:]
          #print(x1,y2)

          fingers = hand.fingersUp(img, draw=False)
          if fingers==2:
              #print(x1,y1)
              mouse.move(x1,y1)
              mouse.position=(x1,y1)
          if fingers==1:
              mouse.press(Button.left)
              mouse.release(Button.left)
              mouse.move(x1, y1)
              mouse.position = (x1, y1)


    #########################
    cTime=time.time()
    fps=1/(cTime-pTime)

    pTime=cTime

    cv.putText(img,str(int(fps)),(30,60),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,200),2)
    cv.imshow("img", resized)
    cv.waitKey(1)





