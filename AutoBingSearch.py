import pyautogui as pg
import configparser
import os

from tqdm import tqdm
from random_word import RandomWords


pg.PAUSE = 0.0

DEFAULT_X = 500
DEFAULT_Y = 125
DEFAULT_LOOP = 32


def ensure_config_file_exists():
    file_name = "config.ini"
    if os.path.exists(file_name):
        return file_name
    else:
        config = configparser.ConfigParser()
        config["default"] = {
            "X": "500",
            "Y": "125",
            "LoopTimes": "32",
        }
        with open(file_name, "w") as configfile:
            config.write(configfile)
    return file_name


def read_saerch_bar_location_and_loop_times():
    filename = ensure_config_file_exists()
    config = configparser.ConfigParser()
    config.read(filename)
    config_value = config["default"]

    x = config_value.getint("X", fallback=DEFAULT_X)
    y = config_value.getint("Y", fallback=DEFAULT_Y)
    loops = config_value.getint("LoopTimes", fallback=DEFAULT_LOOP)
    return (x, y, loops)


def generate_writer():
    r = RandomWords()
    return r.get_random_word()


def main():
    x, y, loop_times = read_saerch_bar_location_and_loop_times()
    for i in tqdm(range(loop_times)):
        pg.moveTo(x, y)  # change with your actual searchbar location
        pg.doubleClick()
        pg.hotkey("ctrl", "a")
        pg.write(generate_writer())
        pg.press("enter")
        pg.sleep(8)


if __name__ == "__main__":
    pg.sleep(3)
    print("processing ...")
    pg.countdown(6)
    main()
