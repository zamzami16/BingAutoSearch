from random_word import RandomWords
from tqdm import tqdm
import configparser
import os
import pyautogui as pg


class AutoGUIBot:
    def __init__(self):
        pg.PAUSE = 0.0
        self.DEFAULT_X = 500
        self.DEFAULT_Y = 125
        self.DEFAULT_LOOP = 32

    def ensure_config_file_exists(self):
        file_name = "config.ini"
        if os.path.exists(file_name):
            return file_name
        else:
            config = configparser.ConfigParser()
            config["default"] = {
                "X": str(self.DEFAULT_X),
                "Y": str(self.DEFAULT_Y),
                "LoopTimes": str(self.DEFAULT_LOOP),
            }
            with open(file_name, "w") as configfile:
                config.write(configfile)
        return file_name

    def read_search_bar_location_and_loop_times(self):
        filename = self.ensure_config_file_exists()
        config = configparser.ConfigParser()
        config.read(filename)
        config_value = config["default"]

        x = config_value.getint("X", fallback=self.DEFAULT_X)
        y = config_value.getint("Y", fallback=self.DEFAULT_Y)
        loops = config_value.getint("LoopTimes", fallback=self.DEFAULT_LOOP)
        return x, y, loops

    def generate_writer(self):
        r = RandomWords()
        return r.get_random_word()

    def perform_interaction(self, x, y, loop_times):
        for i in tqdm(range(loop_times)):
            pg.moveTo(x, y)
            pg.doubleClick()
            pg.hotkey("ctrl", "a")
            pg.write(self.generate_writer())
            pg.press("enter")
            pg.sleep(8)

    def run(self):
        pg.sleep(3)
        print("Processing...")
        pg.countdown(6)
        x, y, loop_times = self.read_search_bar_location_and_loop_times()
        self.perform_interaction(x, y, loop_times)


if __name__ == "__main__":
    bot = AutoGUIBot()
    bot.run()
