from handDetect import Detector, Cap
import sys


"""
Setup working space size
"""

if __name__ == "__main__":

    # Initialize camera, mouse and detector
    cap = Cap(0)
    detector = Detector(cap)

    # Setup detector edges
    detector.get_screen()
    sys.exit(0)