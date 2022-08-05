#####Luckly we do have the module built in already
import math


import HandTrackingModule as hand


import cv2 as cv
import time
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

#################################
pTime=0
wCam,hCam=640,480


#################################
detector=hand.handDetector(detectionCon=0.7)
cap =cv.VideoCapture(0)

###
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#volume.GetMute()
#volume.GetMasterVolumeLevel()
volumeRange=volume.GetVolumeRange()
minVolume =volumeRange[0]
maxVolume=volumeRange[1]

volume.SetMasterVolumeLevel(0, None)
vol=0
volBar=400
volBarPer=0
###

#### hand Range 270-40////volume range -65---(-0)




####

cap.set(3,wCam)
cap.set(5,hCam)



while True :
    success, img= cap.read()
    img=detector.findHands(img)
    result=detector.findPosition(img,draw=False)
    if len(result)!=0:
       # print(result[4],result[8])
        x1,y1=result[4][1],result[4][2]
        cv.circle(img,(x1,y1),15,(255,0,255),cv.FILLED)
        x2, y2 = result[8][1], result[8][2]
        cv.circle(img, (x2, y2), 15, (255, 0, 255), cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cx,cy=(x1+x2)//2,(y2+y1)//2
        cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)
        #####Finding the length of the line
        length = math.hypot(x2-x1,y2-y1)
        vol=np.interp(length,[20,150],[minVolume,maxVolume])###this convert range to a given scale
        volBar = np.interp(length, [20, 150], [400, 150])  ###this convert range to a given scale
        volBarPer = np.interp(length, [400, 150], [0 , 100])  ###this convert range to a given scale

        volume.SetMasterVolumeLevel(vol, None)
        if length<30:
            cv.circle(img, (cx, cy), 15, (255, 0, 0), cv.FILLED)

       # print (vol)
        #print(length)

    cv.rectangle(img,(50,150),(86,480),(0,255,0),3)

    cv.rectangle(img, (50, int(volBar)), (86, 480), (0, 255, 0),cv.FILLED)
    cv.putText(img, str(int(volBarPer))+" %", (120, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv.putText(img,str(int(fps)),(40,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv.imshow("img",img)
    cv.waitKey(1)
