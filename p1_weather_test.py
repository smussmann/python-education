import datetime
import unittest

import p1_weather


class DefaultDataTest(unittest.TestCase):
    def test_high(self):
        high, at = p1_weather.high(p1_weather.data)
        self.assertEqual(high, 60.55)
        self.assertEqual(at, datetime.datetime(2022, 3, 31, 13, 0))

    def test_low(self):
        low, at = p1_weather.low(p1_weather.data)
        self.assertEqual(low, 36.23)
        self.assertEqual(at, datetime.datetime(2022, 4, 2, 6, 0))

    def test_daily_high(self):
        daily_highs = p1_weather.daily_high(p1_weather.data)
        self.assertEqual(
            daily_highs,
            [
                (60.55, datetime.datetime(2022, 3, 31, 13, 0)),
                (57.99, datetime.datetime(2022, 4, 1, 0, 0)),
                (47.44, datetime.datetime(2022, 4, 2, 12, 0)),
            ],
        )

    def test_daily_low(self):
        daily_lows = p1_weather.daily_low(p1_weather.data)
        self.assertEqual(
            daily_lows,
            [
                (54.88, datetime.datetime(2022, 3, 31, 19, 0)),
                (43.32, datetime.datetime(2022, 4, 1, 23, 0)),
                (36.23, datetime.datetime(2022, 4, 2, 6, 0)),
            ],
        )


if __name__ == "__main__":
    unittest.main()
