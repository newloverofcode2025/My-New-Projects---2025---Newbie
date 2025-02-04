import unittest
from game_outcome import gameResult

class TestGameOutcome(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(gameResult([5, 4, 3], [3, 5, 4]), 0)

    def test_alice_wins(self):
        self.assertEqual(gameResult([7, 6, 5], [4, 3, 2]), 1)

    def test_bob_wins(self):
        self.assertEqual(gameResult([2, 8, 1], [7, 3, 9]), -1)

if __name__ == "__main__":
    unittest.main()