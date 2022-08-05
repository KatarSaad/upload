import cv2 as cv                                        #####Remember to allways make your thinking and actions simplar
import numpy as np

import HandTrackingModule as hm

######

######



cap=cv.VideoCapture(0)


wCam,hCam=1000,720
cap.set(3,wCam)
cap.set(4,hCam)

positions=[[5,200],[200,400],[400,600],[600,800]]


hand=hm.handDetector()
colors =[(255,0,0),(0,255,0 ),(0,0,255),(0,0,0)]


points=[]##array of points to draw
xp,yp=0,0
color=(0,0,0)
brush=15
imgCanvas=np.zeros((480,640,3),np.uint8)
while True :

    success,img=cap.read()
    img=cv.flip(img,1)
    img=hand.findHands(img,draw=False )
    #print(img.shape[:2])

    landmark=hand.findPosition(img,draw=False)

    if len(landmark)!=0:

            val=hand.fingersUp(img,draw=False)

            for i  in range(4):
                if landmark[8][2]<100 and val==1:
                    if landmark[8][1]>=positions[i][0] and  landmark[8][1]<=positions[i][1]:

                        color=colors[i]
                        break
            ifx,ify= landmark[8][1] ,landmark[8][2]
            #mfx,mfy=landmark[12][1],landmark[12][1]


            if val==1 or val==2:

                   #points.append([landmark[8][1], landmark[8][2],color])
                   # cv.circle(img,(point[0],point[1]),7,point[2],cv.FILLED)
                   if xp == yp == 0:
                       xp, yp = ifx, ify

                   if color==(0,0,0):
                       brush=28


                   cv.line(img, (xp, yp), (ifx, ify), color,brush)
                   cv.line(imgCanvas, (xp, yp), (ifx, ify), color, brush)
                   xp, yp = ifx ,ify


    '''for point in points :
        #print(point[0])
        #print(point[1])
        #print(point[2])
        #cv.circle(img,(point[0],point[1]),7,point[2],cv.FILLED)
        if xp==yp==0:
            xp,yp=ifx,ify

        cv.line(img,(xp,yp),(ifx,ify),point[2],15)
        cv.line(imgCanvas,(point[0],point[1]),(ifx,ify),point[2],15)

        xp,yp=point[0],point[1]
'''
    img=cv.addWeighted(img,0.5,imgCanvas,0.5,0)

    cv.imshow("img",img)

    cv.imshow("imgCanvass",imgCanvas)

    cv.waitKey(1)



