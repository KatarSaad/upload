from datetime import time
from random import randint

import werkzeug.utils
from flask import Flask , jsonify,request
import cv2

import FaceModule
from HandTrackingModule import handDetector
from Timer import Timer
import time


def readImg(image):
    t = Timer()
    t.start()

    pTime = 0
    cTime = 0
#    cap = cv2.VideoCapture(image)

    detector = handDetector()
    drawRec = FaceModule.FaceDetection

    firstIn = False

    bbox = [50, 100, 200, 200]
    while True:
        stable = True
        #success, img = cap.read()
        img=cv2.imread(image)
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if int(t.timee()) % 3 == 0:
            a = randint(0, 300)
            b = randint(0, 300)

            bbox = [a, b, 200, 200]

        if len(lmList) != 0:
            lx = bbox[0] + bbox[2]
            ly = bbox[1] + bbox[3]
            x = bbox[0]
            y = bbox[1]
            x, y, w, h, = bbox
            x1, y1 = x + w, y + h
            cv2.line(img, (x, y), (x + 10, y), (255, 0, 230), 20)
            cv2.line(img, (x1 - 10, y1), (x1, y1), (255, 0, 230), 20)
            cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (255, 0, 255), 2)

            for hand in lmList:
                if not (hand[1] >= x and hand[1] <= lx and hand[2] >= y and hand[2] <= ly):
                    stable = False
                    break
            if stable:
                cv2.putText(img, "Hand is in", (bbox[1], bbox[2] - 40), cv2.FONT_HERSHEY_PLAIN, 2, (250, 120, 60), 3)
            else:
                cv2.putText(img, "Hand is not in", (bbox[1], bbox[2] - 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 120, 60), 3)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(t.timee())), (130, 130), cv2.FONT_HERSHEY_PLAIN, 2, (0, 240, 230), 4)
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
print(cv2.__version__)

app=Flask (__name__)
@app.route('/upload',methods=["POST"])
def upload():
    if(request.method=="POST"):
        imagefile=request.files['file']
        filename=werkzeug.utils.secure_filename(imagefile.filename)
        img=imagefile.save("imaaaaaaaage.jpg")


        readImg("imaaaaaaaage.jpg")




        return jsonify({
            "message":"Image Uploaded"
        })
    else :
        print ("xxxx")

if __name__ =="__main__":
    app.run()
