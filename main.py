from handDetect import Detector, Cap
from mouseMove import Mouse


settings_file = "setting.txt"

acceleration = 1.5
drag = 2


pos = (-1, -1)
finger_state = False
fingers = 1


def accelerate(vector):
    x = abs(vector[0])
    y = abs(vector[1])

    try:
        sign_x = x / vector[0]
    except ZeroDivisionError:
        sign_x = 1
    try:
        sign_y = y / vector[1]
    except ZeroDivisionError:
        sign_y = 1

    x = x ** acceleration / drag
    y = y ** acceleration / drag

    return sign_x * x, sign_y * y


def check_click():
    global fingers, finger_state
    if fingers[0] and not finger_state:
        finger_state = True
        mouse.click()
    elif not fingers[0] and finger_state:
        finger_state = False


if __name__ == "__main__":

    # Initialize camera, mouse and detector
    cap = Cap(0)
    mouse = Mouse()
    detector = Detector(cap)

    # If not setup flag, get setting from file
    with open("setting.txt", "r") as f:
        detector.screen = list(map(int, f.readline()[1:-1].split(", ")))

    last_pos = (-1, -1)
    while True:
        # Get arm position
        pos = detector.get_pos()
        # Get fingers state
        fingers = detector.fingers

        if pos != (-1, -1) and fingers not in ([0, 0, 0, 0, 0]):
            if last_pos != (-1, -1):
                vector = accelerate((last_pos[0]-pos[0], last_pos[1]-pos[1]))
                mouse.move(*vector)

            check_click()

            last_pos = pos
        else:
            last_pos = (-1, -1)