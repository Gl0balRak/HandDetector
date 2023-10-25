import timeit
from mouseMove import Mouse
from handDetect import Detector, Cap


mouse = Mouse()
cap = Cap(0)
detector = Detector(cap)


# with open("setting.txt", "r") as f:
#     detector.screen = list(map(int, f.readline()[1:-1].split(", ")))


def move():
    mouse.move(30, 10)


def get_pos():
    detector.get_pos()


print(timeit.timeit(move, number=10)/10)
print(timeit.timeit(get_pos, number=10)/10)