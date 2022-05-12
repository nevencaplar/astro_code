import unittest
from CalculateSF import calculate_sf2

class TestReturnValues(unittest.TestCase):
    def test_value(self):
        """
        Test for a known return value
        """
        test_t = np.array([1.11, 2.23, 3.45, 4.01, 5.67, 6.32, 7.88, 8.2])
        test_y = np.array([.11, .23, .45, .01, .67, .32, .88, .2])
        test_yerr = np.array([.1, .023, .045, .1, .067, .032, .8, .02])
        test_bins = [1, 3, 5, 7]
        
        
        self.assertEqual(np.sum(calculate_sf2(test_t, test_y,
                                              test_yerr, test_bins)),
                         -0.0126072883605957)

if __name__  == '__main__':
    unittest.main()