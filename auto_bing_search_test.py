from AutoBingSearch import AutoGUIBot
from config_model import Config
import unittest
from unittest.mock import patch


class TestAutoGUIBot(unittest.TestCase):
    def setUp(self):
        self.bot = AutoGUIBot()
        self.config = Config.from_file_or_default("config.json")

    def test_generate_writer(self):
        word = self.bot.generate_writer()
        self.assertIsInstance(word, str)
        self.assertTrue(len(word) > 0)

    def test_get_random_delay(self):
        delay = self.bot.get_random_delay(self.config)
        min_delay = self.config.global_setting.delay.min
        max_delay = self.config.global_setting.delay.max
        self.assertTrue(min_delay <= delay <= max_delay)

    def test_get_random_location(self):
        item = self.config.data[0]
        x, y = self.bot.get_random_location(item)
        min_x = item.config.pos_x - item.config.d_x
        max_x = item.config.pos_x + item.config.d_x
        min_y = item.config.pos_y - item.config.d_y
        max_y = item.config.pos_y + item.config.d_y
        self.assertTrue(min_x <= x <= max_x)
        self.assertTrue(min_y <= y <= max_y)

    def test_get_random_scroll(self):
        scroll = self.bot.get_random_scroll()
        self.assertTrue(500 <= scroll <= 1000)

    @patch("pyautogui.moveTo")
    @patch("pyautogui.doubleClick")
    @patch("pyautogui.hotkey")
    @patch("pyautogui.write")
    @patch("pyautogui.press")
    @patch("pyautogui.sleep")
    @patch("pyautogui.scroll")
    def test_perform_interaction(
        self,
        mock_scroll,
        mock_sleep,
        mock_press,
        mock_write,
        mock_hotkey,
        mock_doubleClick,
        mock_moveTo,
    ):
        # Only test one iteration for speed
        test_config = self.config
        test_config.global_setting.total_search = 1
        self.bot.perform_interaction(test_config)
        self.assertTrue(mock_moveTo.called)
        self.assertTrue(mock_doubleClick.called)
        self.assertTrue(mock_hotkey.called)
        self.assertTrue(mock_write.called)
        self.assertTrue(mock_press.called)
        self.assertTrue(mock_sleep.called)
        self.assertTrue(mock_scroll.called)


if __name__ == "__main__":
    unittest.main()
