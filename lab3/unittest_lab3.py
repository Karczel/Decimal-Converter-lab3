"""Test code"""
import unittest
from functions import*

class DecimalConverter(unittest.TestCase):
    """Test cases"""
    def test_tobin(self):
        """to binary"""
        print('Test cases')
        self.assertEqual(111,dec_to_bin(7))
        print('-------------------------------------------------------')

    def test_tobase(self):
        """to base y"""
        self.assertEqual(10,dec_to_base_y(7, 7))
        self.assertEqual(21,dec_to_base_y(7, 3))
        self.assertEqual(dec_to_bin(7),dec_to_base_y(7, 2))
        print('-------------------------------------------------------')


    def test_todec(self):
        """to decimal"""
        print()
        self.assertEqual(bin_to_dec(111),7)
        self.assertEqual(bin_to_dec(110),6)
        self.assertEqual(bin_to_dec(101001),41)
        self.assertEqual(base_y_to_dec(1231231, 4),7021)
        self.assertEqual(base_y_to_dec(10, 7),7)
        self.assertEqual(base_y_to_dec(21, 3),7)
        print('-------------------------------------------------------')

    def test_lab3_question2(self):
        """From Lab3 question:
                Demonstrate how you can convert the 1873 base 10
                to the equivalent number
                in base 2, base 7, and base 8."""
        print('\nTests from question 1:')
        print(dec_to_bin(1873))
        print(dec_to_base_y(1873, 7))
        print(dec_to_base_y(1873, 8))
        print('-------------------------------------------------------')

if __name__=='__main__':
    unittest.main()