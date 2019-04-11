import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_NONE(self):
        """Tests the max_list_iter function for if ValueError is raised correctly"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
   
    def test_max_list_iter_DUPLICATES(self):
        """Tests the max_list_iter function by passing in list of duplicates"""
        tlist = [4, 4, 4, 4]
        self.assertEqual(max_list_iter(tlist), 4)
   
    def test_max_list_iter_NORMAL(self):
        """Tests the max_list_iter funciton with list of different values"""
        tlist1 = [1, 2, 3, 4]
        self.assertEqual(max_list_iter(tlist1), 4)
        tlist2 = [1, 2, 4, 3]
        self.assertEqual(max_list_iter(tlist2), 4)
        tlist3 = [1, 4, 2, 3]
        self.assertEqual(max_list_iter(tlist3), 4)
        tlist4 = [4, 1, 2, 3]
        self.assertEqual(max_list_iter(tlist4), 4)

    def test_max_list_iter_NONE_2(self):
        """Tests max_list_iter with list of None"""
        tlist = [None, None, None]
        self.assertEqual(max_list_iter(tlist), 0)
        tlist2 = [None, 2, -1]
        self.assertEqual(max_list_iter(tlist2), 2)

    def test_max_list_iter_nonints(self):
        """Tests max_list_iter with strings and floats"""
        self.assertEqual(max_list_iter([1.2, 2.8, 5, 7.0]), 7.0)
        self.assertEqual(max_list_iter(["hi", "hello", 2, 5, 3.0]), 5)

    def test_max_list_iter_EMPTY(self):
        """Tests the max_list_iter function by passing in empty list"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_reverse_rec(self):
        """Tests reverse_rec with list of values"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1, 3, 3, 4]), [4, 3, 3, 1])
        self.assertEqual(reverse_rec([3, 1, 3]), [3, 1, 3])
        self.assertEqual(reverse_rec(['hello', 3, 5.0, 'hi']), ['hi', 5.0, 3, 'hello'])
        self.assertEqual(reverse_rec([3, 3, 3]), [3, 3, 3])

    def test_reverse_rec_2(self):
        """Tests reverse_rec with some values being None"""
        self.assertEqual(reverse_rec([None, 2, 3, 5]), [5, 3, 2, None])
        self.assertEqual(reverse_rec([None, None, None]), [None, None, None])
        self.assertEqual(reverse_rec([1, None, None]), [None, None, 1])
       
    def test_reverse_rec_3(self):
        """Tests reverse_rec with 2D list"""
        self.assertEqual(reverse_rec([[1, 2], 3, [4, 5]]), [[4, 5], 3, [1, 2]])
       
    def test_reverse_rec_4(self):
        """Tests reverse_rec with floats and strings"""
        self.assertEqual(reverse_rec(["hello"]), ["hello"])
        self.assertEqual(reverse_rec([1.2, 2.0, 3.5]), [3.5, 2.0, 1.2])
        
    def test_reverse_rec_EMPTY(self):
        """Tests reverse_rec with empty list"""   
        self.assertEqual(reverse_rec([]), None)

    def test_reverse_rec_NONE(self):
        """Tests reverse_rec with None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist) 

    def test_bin_search_1(self):
        """Tests bin_search when target is in lower bound"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search_2(self):
        """Tests bin_search when target is not in list"""
        list_val = [-3, 0, 1, 4, 8, 20]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, low, high, list_val), None)

    def test_bin_search_4(self):
        """Tests bin_search with duplicate values in list"""
        list_val = [3, 3, 3, 4, 5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, low, high, list_val), 2)

    def test_bin_search_5(self):
        """Tests bin_search with duplicate values in list with even number of indices"""
        list_val = [1, 2, 3, 4, 5, 5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, low, high, list_val), 4)

    def test_bin_serach_6(self):
        """Tests bin search when value is in upper bound"""
        list_val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(7, low, high, list_val), 7)

    def test_bin_search_7(self):
        """Tests bin search when value is in lower bound"""
        list_val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(2, low, high, list_val), 2)

    def test_bin_search_8(self):
        """Tests bin search when value cannot be found and None is returned"""
        list_val = [1, 3, 5]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(2, low, high, list_val), None)

    def test_bin_search_9(self):
        """Tests bin search with a ridiculous amount of indices where target is found"""
        list_val = list(range(0, 100))
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(60, low, high, list_val), 60)

    def test_bin_search_10(self):
        "Tests bin search with a ridiculous amount of indices where target is not found"""
        list_val = list(range(1, 100, 2))
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(40, low, high, list_val), None)

    def test_bin_search_11(self):
        "Tests bin search with a high value less than the low value"""
        list_val = [1, 2, 3, 4, 5]
        low = 5
        high = 4
        self.assertEqual(bin_search(3, low, high, list_val), None)

    def test_bin_search_12(self):
        """Tests bin search with negative numbers"""
        list_val = [-10, -9, -8, -7, -3]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(-7, low, high, list_val), 3)
        self.assertEqual(bin_search(-2, low, high, list_val), None)
        list_val_2 = [-10, -9, -8, -7, -3, 0]
        low = 0
        high = len(list_val_2) - 1
        self.assertEqual(bin_search(0, low, high, list_val_2), 5)

    def test_bin_search_13(self):
        """Tests bin_search when target is in middle"""
        list_val = [1, 2, 3, 4, 5]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(3, low, high, list_val), 2)
        list_val_2 = [1, 2, 3, 4, 5, 6]
        high = len(list_val_2) - 1
        self.assertEqual(bin_search(4, low, high, list_val), 3)

    def test_bin_search_14(self):
        """Tests when target is in decimal form"""
        list_val = [1.0, 2.0, 3.5, 4.8]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(2.0, low, high, list_val), 1)        

    def test_bin_search_NONE(self):
        """Tests bin_search with None"""
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(4, 0, 5, tlist)

    def test_bin_search_EMPTY(self):
        """Tests bin_search with empty list"""
        tlist = []
        self.assertEqual(bin_search(4, 0, len(tlist)-1, tlist), None)

if __name__ == "__main__":
        unittest.main()

    
