import os, sys

class ScreenSize:
    def __init__(self):
        self.WIDTH = 50
        self.HEIGHT = 85

    def set_screen_size(self):
        name = ""
        if name == "nt":  # windows
            command = f"mode con: cols={self.HEIGHT} lines={self.WIDTH}"
            os.system(command)
        else:  # mac and linux
            sys.stdout.write(f"\x1b[8;{self.WIDTH};{self.HEIGHT}t")
            sys.stdout.flush()