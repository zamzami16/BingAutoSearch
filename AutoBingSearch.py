import pyautogui as pg
from tqdm import tqdm
from random_word import RandomWords


pg.PAUSE = 0.1


def generate_writer(length=10):
    r = RandomWords()
    return r.get_random_word()


def main():
    numSearch = 32
    for i in tqdm(range(numSearch)):
        pg.moveTo(500, 125)  # change with your actual searchbar location
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
