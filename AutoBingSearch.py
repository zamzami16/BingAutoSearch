from random_word import RandomWords
from tqdm import tqdm
import pyautogui as pg
from random import Random

from config_model import Config, DataItem


class AutoGUIBot:
    def __init__(self):
        pg.PAUSE = 0.01

    def generate_writer(self):
        r = RandomWords()
        return r.get_random_word()

    def get_random_delay(self, config: Config) -> int:
        r = Random()
        val = r.randint(
            config.global_setting.delay.min, config.global_setting.delay.max
        )
        return val

    def get_random_location(self, item: DataItem) -> tuple[int, int]:
        r = Random()
        min_x, max_x = (
            item.config.pos_x - item.config.d_x,
            item.config.pos_x + item.config.d_x,
        )
        min_y, max_y = (
            item.config.pos_y - item.config.d_y,
            item.config.pos_y + item.config.d_y,
        )
        x = r.randint(min_x, max_x)
        y = r.randint(min_y, max_y)
        return x, y

    def get_random_scroll(self, config: Config) -> int:
        r = Random()
        val = r.randint(
            config.global_setting.scroll.min, config.global_setting.scroll.max
        )
        return val

    def perform_interaction(self, config: Config):
        for i in tqdm(range(config.global_setting.total_search)):
            for item in config.data:
                x, y = self.get_random_location(item)
                pg.moveTo(x, y)
                pg.doubleClick()
                pg.hotkey("ctrl", "a")
                pg.write(self.generate_writer())
                pg.press("enter")
                pg.sleep(self.get_random_delay(config))
                pg.moveTo(x, y + 200)

                r = Random()
                n_scroll = r.randint(
                    config.global_setting.total_scroll.min,
                    config.global_setting.total_scroll.max,
                )
                for _ in range(n_scroll):
                    scroll_val = self.get_random_scroll(config)
                    direction = r.choice([-1, 1])
                    pg.scroll(direction * scroll_val)
                    pg.sleep(self.get_random_delay(config))

    def run(self):
        pg.sleep(3)
        print("Processing...")
        pg.countdown(6)
        config = self.get_config()
        self.perform_interaction(config)

    def get_config(self):
        return Config.from_file_or_default("config.json")


if __name__ == "__main__":
    bot = AutoGUIBot()
    bot.run()
