from mouseMove import Mouse
from time import sleep


if __name__ == "__main__":
    mouse = Mouse()

    dots = [(1, 1), (5, 5), (6, 15), (11, -20), (-21, 0), (30, 30), (-15, 3), (-10, -13), (-5, -20)]

    for dot in dots:
        mouse.move(*dot)
        print(f"Move {dot}")
        sleep(1)