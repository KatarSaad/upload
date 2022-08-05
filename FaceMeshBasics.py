import cv2 as cv
import mediapipe as mp
import time

import FaceMeshModule

pTime=0
mpDraw=mp.solutions.drawing_utils
mpMesh=mp.solutions.face_mesh
faceMesh=mpMesh.FaceMesh(max_num_faces=2)
drawSpecs=mpDraw.DrawingSpec(thickness=1,color=(255,60,120),circle_radius=1)
cap =cv.VideoCapture(0)
mesh=FaceMeshModule.FaceMesh()


counter=0
bol=True
while True :
    succes,img=cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)

    img,face=mesh.getMesh(img)
    f=face[0]
    if len(f)!=0:

        cv.putText(img, str(f[23][2]), (240, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        cv.putText(img, str(f[159][2]), (320, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        lb=f[23][2]
        lt=f[159][2]
        ll=f[130][1]
        lr=f[243][1]
        blink=int((lb-lt)/(lr-ll)*100)
        if blink<=30:
            if bol:
               counter+=1
               bol=False
        else :
            bol=True

        cv.putText(img, str(counter), (190, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
        cv.putText(img, str(blink), (100, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,135, 40), 2)
    ''' for face_landmark in results.multi_face_landmarks:

            mpDraw.draw_landmarks(img,face_landmark,mpMesh.FACEMESH_CONTOURS,drawSpecs,drawSpecs)
            for id ,lm in enumerate(face_landmark.landmark):
                #print(lm)
                h,w,c=img.shape
                x,y=int (lm.x*w), int(lm.y*h)
                print(id,x,y)
    '''


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

   # cv.putText(img, str(int(fps)), (20, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

    cv.imshow("Video", img)
    cv.waitKey(1)