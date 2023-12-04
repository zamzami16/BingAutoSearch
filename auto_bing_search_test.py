from AutoBingSearch import AutoGUIBot
from unittest.mock import patch
import os
import shutil
import unittest


class TestAutoGUIBot(unittest.TestCase):
    def setUp(self):
        file_name = "config.ini"

        if os.path.exists(file_name):
            os.remove(file_name)

        self.bot = AutoGUIBot()

    def tearDown(self):
        file_name = "config.ini"
        backup_file_name = "config.ini.bk"

        if os.path.exists(file_name):
            os.remove(file_name)

        if os.path.exists(backup_file_name):
            shutil.copy(backup_file_name, file_name)

    @patch("builtins.input", return_value="y")
    def test_ensure_config_file_exists(self, mock_input):
        file_name = self.bot.ensure_config_file_exists()
        self.assertTrue(os.path.exists(file_name))
        with open(file_name, "r") as configfile:
            content = configfile.read().upper()
            self.assertIn("Y = ".upper(), content)
            self.assertIn("X = ".upper(), content)
            self.assertIn("LoopTimes = ".upper(), content)

    def test_read_search_bar_location_and_loop_times(self):
        x, y, loop_times = self.bot.read_search_bar_location_and_loop_times()
        self.assertEqual(x, self.bot.DEFAULT_X)
        self.assertEqual(y, self.bot.DEFAULT_Y)
        self.assertEqual(loop_times, self.bot.DEFAULT_LOOP)

        # Create a custom config file for testing
        config_content = "[default]\nX = 600\nY = 150\nLoopTimes = 20"
        with open("config.ini", "w") as configfile:
            configfile.write(config_content)

        x, y, loop_times = self.bot.read_search_bar_location_and_loop_times()
        self.assertEqual(x, 600)
        self.assertEqual(y, 150)
        self.assertEqual(loop_times, 20)

    def test_generate_writer(self):
        word = self.bot.generate_writer()
        self.assertTrue(isinstance(word, str))
        self.assertTrue(len(word) > 0)

    @patch("pyautogui.moveTo")
    @patch("pyautogui.doubleClick")
    @patch("pyautogui.hotkey")
    @patch("pyautogui.write")
    @patch("pyautogui.press")
    @patch("pyautogui.sleep")
    def test_perform_interaction(
        self,
        mock_sleep,
        mock_press,
        mock_write,
        mock_hotkey,
        mock_doubleClick,
        mock_moveTo,
    ):
        self.bot.perform_interaction(self.bot.DEFAULT_X, self.bot.DEFAULT_Y, 1)

        # Check the expected calls
        mock_moveTo.assert_called_once_with(
            self.bot.DEFAULT_X, self.bot.DEFAULT_Y
        )
        mock_doubleClick.assert_called_once()
        mock_hotkey.assert_called_once_with("ctrl", "a")
        mock_write.assert_called_once()
        mock_press.assert_called_once_with("enter")
        mock_sleep.assert_called_once_with(8)


if __name__ == "__main__":
    unittest.main()
