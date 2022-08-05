import cv2 as cv
import mediapipe as mp
import time
pTime=0
cap= cv.VideoCapture(0)
mpPose=mp.solutions.pose
pose=mpPose.Pose()
mpDraw=mp.solutions.drawing_utils
while True:
    succes,img=cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    if results.pose_landmarks :
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape


            cx,cy=int(lm.x*w),int(lm.y*h)
            cv.circle(img,(cx,cy),5,(255,255,0),cv.FILLED)

            print(id,lm)



    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime = cTime
    cv.putText(img,str(int(fps)),(20,70),cv.FONT_HERSHEY_DUPLEX,3,(0,0,255),2)

    cv.imshow("video", img)



    cv.waitKey(1)
