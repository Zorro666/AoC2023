import day01
import unittest

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(day01.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(day01.decrement(3), 2)

if __name__ == '__main__':
    unittest.main()
