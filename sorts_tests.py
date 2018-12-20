import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    # def test_selection_sort(self):
        # nums = [23, 10, 5 , 3, 18, 4, 4]
        # comps = selection_sort(nums)
        # print('selection comps', comps)
        # self.assertEqual(comps, 21)
        # nums = [5,4]
        # comps = selection_sort(nums)
        # self.assertEqual(comps, 1)
        # # self.assertEqual(nums, [10, 23])
        # with self.assertRaises(IndexError):
        #     selection_sort(None)
        # nums = [4]
        # comps = selection_sort(nums)
        # print('selection comps', comps)
        # self.assertEqual(comps, 0) 
    
    def test_insertion_sort(self):
        nums = [8, 7, 6, 5, 4, 3, 2, 1] #worst case list
        comps = insertion_sort(nums)
        print('insertion comps', comps)
        self.assertEqual(comps, 28)
        
        nums = [1,2,3,4,5,6,7,8]
        comps = insertion_sort(nums)
        print('insertion comps', comps)
        self.assertEqual(comps, 7)
        
        nums = [23,10]
        comps = insertion_sort(nums)
        print('insertion comps', comps)
        self.assertEqual(comps, 1)
        
        nums = [0]
        comps = insertion_sort(nums)
        print('insertion comps', comps)
        self.assertEqual(comps, 0)
        
        with self.assertRaises(IndexError):
            selection_sort(None)
       
        

if __name__ == '__main__': 
    unittest.main()
