import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc1 = Location("SLO", 35.30, -120.70)
        loc2 = Location("SLO", 35.3, -120.70)
        self.assertEqual(loc1, loc2)
        self.assertEqual(loc1, Location("SLO", 35.30, -120.70))

if __name__ == "__main__":
        unittest.main()
