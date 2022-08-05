import cv2 as cv
import time
pTime=0
import mediapipe as mp
cap=cv.VideoCapture(0)
mpFaceDetect=mp.solutions.face_detection
face=mpFaceDetect.FaceDetection()
mpDraw=mp.solutions.drawing_utils




while True:
    succes ,img=cap.read()
    #convert the img
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=face.process(imgRGB)
    if results.detections:

         for id,detection in enumerate(results.detections):
             #mpDraw.draw_detection(img,detection)
             #print(detection.score)
             #print(detection.location_data.relative_bounding_box)
             bboxC=detection.location_data.relative_bounding_box
             h,w,c=img.shape
             bbox=int (bboxC.xmin*w),int (bboxC.ymin
                                          *h), \
                  int(bboxC.width * w), int(bboxC.height * h)
             cv.rectangle(img,(bbox[0],bbox[1]),(bbox[0]+bbox[2],bbox[1]+bbox[3]),(255,0,255),2)
             cv.putText(img,f"conf:{int(detection.score[0]*100)}%",(bbox[0]-10,bbox[1]-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)




    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv.putText(img,"fps"+str(int(fps)),(30,70),cv.FONT_ITALIC,1,(0,255,0),2)
    cv.imshow("img",img)
    cv.waitKey(1)#speed increased
