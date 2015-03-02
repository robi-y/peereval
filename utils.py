class Utils:

    @classmethod
    def complements(cls, a, b):
        return [item for item in a if item not in b]

import unittest

class TestUtils(unittest.TestCase):

    def test_remaining(self):
        remaining = Utils.complements(['a', 'b', 'c', 'd'], ['b','d'])
        self.assertEquals(remaining, ['a', 'c'])

if __name__ == '__main__':
    unittest.main()