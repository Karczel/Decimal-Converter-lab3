from q2 import*

if __name__ == '__main__':
    """Test cases"""
    print(dec_to_bin(7))
    print(dec_to_base_y(7, 7))
    print(dec_to_base_y(7, 3))
    print(dec_to_base_y(7, 2))
    print('---')

    """In thr reverse direction"""
    print(bin_to_dec(111))
    print(bin_to_dec(110))
    print(bin_to_dec(101001))
    print(base_y_to_dec(1231231,4))
    print(base_y_to_dec(10,7))
    print(base_y_to_dec(21,3))
    print('---')

    """Hexadecimal"""
    print(dec_to_hex(120))

    """From Lab3 question:
        Demonstrate how you can convert the 1873 base 10 
        to the equivalent number 
        in base 2, base 7, and base 8."""
    print('\nTests from question 1:')
    print(dec_to_bin(1873))
    print(dec_to_base_y(1873, 7))
    print(dec_to_base_y(1873, 8))
    print('---')

    """Question 4"""
    l1 = 3410
    l2 = 'FF7F'
    l3 = '017037'
    l4 = 1111101110110100
    print('\n4 lines to solve: Decimal, Hexadecimal,Octal,Binary')
    print("Assume 16-bit and two's complememt")
    print('\nLine 1')
    print(f'Decimal number is {l1}')
    # print(f'Hexadecimal number is {}')
    print(f'Octal number is {dec_to_base_y(l1,8)}')
    print(f'Binary number is 0{dec_to_bin(l1)}')
    print('\nLine 2')
    # print(f'Decimal number is {}')
    print(f'Hexadecimal number is {l2}')
    # print(f'Octal number is {}')
    # print(f'Binary number is {}')
    print('\nLine 3')
    print(f'Decimal number is {base_y_to_dec(17037,8)}')
    # print(f'Hexadecimal number is {}')
    print(f'Octal number is {l3}')
    print(f'Binary number is 0{dec_to_bin(base_y_to_dec(17037,8))}')
    print('\nLine 4')
    print(f'Decimal number is {-bin_to_dec(10001001011)}')
    # print(f'Hexadecimal number is {}')
    print(f'Octal number is 77777 - {dec_to_base_y(bin_to_dec(10001001011),8)} +1 (leading 7s to indicate negative)')
    print(f'Binary number is {l4}')


