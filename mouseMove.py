import pyautogui as pg
from pynput.mouse import Controller, Button


class Mouse(Controller):
    def __init__(self):
        super(Mouse, self).__init__()

        self.width = pg.size().width
        self.height = pg.size().height

    def move(self, x, y):
        super(Mouse, self).move(int(x / 100 * self.width), int(y / 100 * self.height))

    def click(self):
        super(Mouse, self).click(Button.left)
