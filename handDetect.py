import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import time


settings_file = "setting.txt"


def constrain(x, a, b):
    return max(min(x, b), a)


def maps(x, a, b, c, d, const=False):
    try:
        if const:
            return constrain((x-b)/(a-b)*(c-d) + d, c, d)
        return (x-b)/(a-b)*(c-d) + d
    except ZeroDivisionError:
        return c


class Cap(cv.VideoCapture):
    """
    Camera class
    """
    def __init__(self, x=0):
        """
        :param x: Number of using camera, default 0.
        """

        super().__init__(x)
        self.set(3, 1920)
        self.set(4, 1080)


class Detector:
    """
    Detecting hands using cvzone class.
    """
    def __init__(self, cap):
        """
        :param cap: Camera to get image.
        """

        self.detector = HandDetector(maxHands=2, detectionCon=0.2)
        self.cap = cap
        self.hand = None
        self.screen = [0, 0, 0, 0]
        self.fingers = 0

    def get_finger(self):
        if self.hand:
            tipIds = [4, 8, 12, 16, 20]
            myHandType = self.hand["type"]
            myLmList = self.hand["lmList"]
            if myHandType == "Right":
                if myLmList[tipIds[0]][0] > myLmList[tipIds[0] - 1][0]:
                    fingers = 1
                else:
                    fingers = 0
            else:
                if myLmList[tipIds[0]][0] < myLmList[tipIds[0] - 1][0]:
                    fingers = 1
                else:
                    fingers = 0

            return fingers
        return 1

    def get_pos(self, absolute=False, show=False, text=""):
        try:
            success, img = self.cap.read()
        except:
            return -1, -1

        if show:
            hands, img = self.detector.findHands(img, draw=True)
            # get boundary of this text
            textsize = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, 2, 2)[0]

            # get coords based on boundary
            textX = int((img.shape[1] - textsize[0]) / 2)
            textY = int((img.shape[0] + textsize[1]) / 2)

            cv.putText(img, text, (textX, textY), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            cv.imshow("Image", img)
            cv.waitKey(1)
        else:
            hands = self.detector.findHands(img, draw=False)

        if hands:
            self.hand = hands[0]
            self.fingers = self.detector.fingersUp(hands[0])

            if absolute: return hands[0]["lmList"][8]
            return (maps(hands[0]["lmList"][0][0], self.screen[1], self.screen[0], 0, 100),
                    maps(hands[0]["lmList"][0][1], self.screen[3], self.screen[2], 0, 100))
        return -1, -1

    def get_screen(self):
        pos = (-1, -1)
        while pos == (-1, -1):
            pos = self.get_pos(absolute=True, show=True)

        screen = [-1, -1, -1, -1]
        messages = ["left", "right", "up", "down"]

        for i in range(4):
            current_time = time.perf_counter()
            while time.perf_counter() - current_time < 3:
                pos = self.get_pos(absolute=True, show=True, text=messages[i])

            screen[i] = pos[[0, 0, 1, 1][i]]

        with open(settings_file, "w") as f:
            f.write(str(screen))

        self.screen = screen