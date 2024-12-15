import cap as cap
import cv2
import time
import numpy as np
import hand_tracking_module as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

ptime=0
ctime=0
capture = cv2.VideoCapture(0)
detector = htm.HandTracking(detection_confidence=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#olume.GetMasterVolumeLevel()
print(volume.GetVolumeRange())
volrange = volume.GetVolumeRange()
minVol = volrange[0]
maxVol = volrange[1]
volume.SetMasterVolumeLevel(0, None)


while True:
    success, img = capture.read()
    detector.find_hands(img)
    lmlist = detector.find_position(img)
    if len(lmlist)!=0:
       # print(lmlist[4],lmlist[8])

        a1,b1= lmlist[4][1],lmlist[4][2]
        a2,b2= lmlist[8][1],lmlist[8][2]
        ca,cb= (a1+a2)//2, (b1+b2)//2
        cv2.circle(img,(a1,b1),3,(255,0,0),3,cv2.FILLED)
        cv2.circle(img, (a2, b2), 3, (255, 0, 0), 3, cv2.FILLED)
        cv2.circle(img, (ca, cb), 3, (255, 0, 0), 3, cv2.FILLED)
        cv2.line(img,(a1,b1),(a2,b2),(255,0,0),3)
        cv2.circle(img, (ca, cb), 3, (255, 0, 0), 3, cv2.FILLED)

        # to find hypotenuse:
        length = math.hypot(a2-a1, b2-b1)
        print(length)
        vol = np.interp(length, [30,100],[minVol,maxVol])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)
        if length<30:
            cv2.circle(img, (ca, cb), 3, (0, 255, 0), 3, cv2.FILLED)
        if length>130:
            cv2.circle(img, (a1, b1), 3, (0, 0, 255), 3, cv2.FILLED)
            cv2.circle(img, (a2, b2), 3, (0, 0, 255), 3, cv2.FILLED)



    ctime= time.time()
    fps= 1/(ptime-ctime)
    ptime=ctime


    cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_TRIPLEX,1 ,(255,0,0),3)
    cv2.imshow("image", img)
    cv2.waitKey(1)