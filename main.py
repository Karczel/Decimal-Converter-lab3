"""Test code"""
import unittest
from q2 import*

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


    def test_hexadecimal(self):
        """Hexadecimal"""
        self.assertEqual(78,int(dec_to_hex(120)))
        self.assertEqual(893247,hex_to_dec('DA13F'))
        print('-------------------------------------------------------')

    def test_complement(self):
        """check if value is negative (leading 1, 7, F, etc)
        and if it is, return complement value"""

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


    def test_lab3_question4(self):
        """Question 4"""
        l1 = 3410
        l2 = 'FF7F'
        l3 = '017037'
        l4 = '1111 1011 1011 0100'
        print('\n4 lines to solve: Decimal, Hexadecimal,Octal,Binary')
        print("Assume 16-bit and two's complememt")
        print('\nLine 1')
        print(f'Decimal number is {l1}')
        print(f'Hexadecimal number is {dec_to_hex(l1)}')
        print(f'Octal number is {dec_to_base_y(l1, 8)}')
        print(f'Binary number is 0{dec_to_bin(l1)} (leading zero to indicate positive)')
        print('\nLine 2')
        # print(f'Decimal number is -{hex_to_dec(hex_complement(l2))}')
        print(f'Decimal number is -{hex_to_dec("0081")}')
        print(f'Hexadecimal number is {l2}')
        # print(f'Octal number is 7777 7777 7777 7777 - {dec_to_base_y(hex_to_dec(hex_complement(l2)), 8)}')
        print(f'Octal number is 7777 7777 7777 7777 - {dec_to_base_y(hex_to_dec("0081"), 8)} + 1 (leading 7s to indicate negative)')
        # print(f'Binary number is 1111 1111 1111 1111 - {dec_to_bin(hex_to_dec(hex_complement(l2)))} + 1')
        print(f'Binary number is 1111 1111 1111 1111 - {dec_to_bin(hex_to_dec("0081"))} + 1 (leading 1s to indicate negative)')
        print('\nLine 3')
        print(f'Decimal number is {base_y_to_dec(17037, 8)}')
        print(f'Hexadecimal number is {dec_to_hex(base_y_to_dec(17037, 8))}')
        print(f'Octal number is {l3}')
        print(f'Binary number is 0{dec_to_bin(base_y_to_dec(17037, 8))} (leading zero to indicate positive)')
        print('\nLine 4')
        print(f'Decimal number is {-bin_to_dec(10001001011)}')
        print(f'Hexadecimal number is FFFF FFFF FFFF FFFF- {dec_to_hex(bin_to_dec(10001001011))} + 1 (leading Fs to indicate negative)')
        print(
            f'Octal number is 7777 7777 7777 7777 - {dec_to_base_y(bin_to_dec(10001001011), 8)} +1 (leading 7s to indicate negative)')
        print(f'Binary number is {l4}')
        print('-------------------------------------------------------')


if __name__=='__main__':
    unittest.main()