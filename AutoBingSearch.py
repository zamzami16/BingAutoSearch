import pyautogui as pg
import random, string
from random_word import RandomWords


pg.PAUSE = 0.1


def generate_writer(length=10):
    r = RandomWords()

    # Return a single random word
    return r.get_random_word()


def main():
    for i in range(32):
        pg.moveTo(500, 125)
        pg.doubleClick()
        pg.hotkey("ctrl", "a")
        pg.write(generate_writer())
        pg.press("enter")
        pg.sleep(8)


if __name__ == "__main__":
    pg.sleep(3)
    pg.countdown(6)
    main()
