import cv2
import mediapipe as mp
import time

class HandTracking:
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, model_complexity=1, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.model_complexity = model_complexity
        self.track_confidence = track_confidence
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode, self.max_hands, self.model_complexity, self.detection_confidence, self.track_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks and draw:
            for handlms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handlms, self.mphands.HAND_CONNECTIONS)

        return img

    def find_position(self, img, hand_no=0):
        lmlist = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if id==0:
                    cv2.circle(img,(cx,cy),1,(255,0,0),5, cv2.FILLED)

        return lmlist

    def display_fps(self, img, pTime):
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_TRIPLEX, 3, (0, 255, 235), 5)
        return img, pTime

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = HandTracking()

    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lmlist = detector.find_position(img)
        if len(lmlist) != 0:
            print(lmlist[0])
        img, pTime = detector.display_fps(img, pTime)
        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()