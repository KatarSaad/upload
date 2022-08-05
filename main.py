import cv2 as cv
import mediapipe as mp
import time
track = []
cap=cv.VideoCapture(0)
cap. set(cv.CAP_PROP_FPS, 60)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
pTime=curenTime=0
while True :
    succes,img=cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
   # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:
              for id ,lm in enumerate(handLms.landmark):

                  h,w,c=img.shape
                  cx,cy=int (lm.x*w),int(lm.y*h)
                  #print(id,cx,cy)

                  if  id==4:
                      track.append( [cx, cy])
                      cv.circle(img,(cx,cy),15,(0,255,0),cv.FILLED)

              mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
   # print(track)

    #if len(track)!=0:

        #for point in track:

         #   cv.circle(img, (point[0],point[1]), 15, (0, 255, 0), cv.FILLED)
          #  print("done")

    curenTime=time.time()
    fps=1/(curenTime-pTime)
    pTime=curenTime
    cv.putText(img,str(int(fps)),(10,90),cv.FONT_ITALIC,3,(255,0,255),3)
    cv.imshow("img",img)
    cv.waitKey(1)
