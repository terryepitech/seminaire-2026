import os
import sys
import unittest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from pomodoro import DEFAULT_DURATIONS, get_duration, format_seconds


class TestPomodoro(unittest.TestCase):

    def test_get_duration_known_modes(self):
        self.assertEqual(get_duration("work"), 25 * 60)
        self.assertEqual(get_duration("short_break"), 5 * 60)
        self.assertEqual(get_duration("long_break"), 15 * 60)

    def test_get_duration_unknown_mode_returns_work_default(self):
        self.assertEqual(get_duration("invalid_mode"), DEFAULT_DURATIONS["work"])

    def test_format_seconds(self):
        cases = [
            (0, "00:00"),
            (5, "00:05"),
            (60, "01:00"),
            (125, "02:05"),
            (3599, "59:59"),
        ]
        for seconds, expected in cases:
            with self.subTest(seconds=seconds):
                self.assertEqual(format_seconds(seconds), expected)


if __name__ == "__main__":
    unittest.main()
