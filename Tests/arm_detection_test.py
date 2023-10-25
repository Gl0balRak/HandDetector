from handDetect import Detector, Cap


if __name__ == "__main__":
    cap = Cap(0)
    detector = Detector(cap)

    with open("../setting.txt", "r") as f:
        detector.screen = list(map(int, f.readline()[1:-1].split(", ")))

    while True:
        print("Arms position:", detector.get_pos(show=True, absolute=True))
        print("Fingers position:", detector.fingers)