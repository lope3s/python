import unittest
from app import makeMessage, roll_dice, roll_dice_multiple_times


class TestHello(unittest.TestCase):

    def test_message(self):
        message = makeMessage(5)
        self.assertEqual(message, "You rolled 5.")

    def test_roll_dice(self):
        for _ in range(100000):
            value = roll_dice()
            self.assertLessEqual(
                value, 6, "Expect to result be less or equal to 6")
            self.assertGreaterEqual(
                value, 1, "Expect result to be greater or equal to 1")

    def test_roll_dice_multiple_times(self):
        values = roll_dice_multiple_times(2)

        self.assertEqual(len(values), 2)

    def test_roll_dice_multiple_times_without_arguments(self):
        values = roll_dice_multiple_times()

        self.assertEqual(len(values), 1)


if __name__ == "__main__":
    unittest.main()
