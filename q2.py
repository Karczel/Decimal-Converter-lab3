"""question 2"""


def dec_to_bin(x):
    """x -> base 10 number to base 2 (str)"""
    if x == 0:
        return 0
    return x % 2 + 10 * dec_to_bin(x // 2)


def dec_to_base_y(x: int, y: int):
    """x -> base 10 number to base y (str)"""
    if x == 0:
        return 0
    return x % y + 10 * dec_to_base_y(x // y, y)


def bin_to_dec(x):
    if x == 0:
        return 0
    return x % 10 + 2 * bin_to_dec(x // 10)


def base_y_to_dec(x: int, y: int):
    if x == 0:
        return 0
    return x % 10 + y * base_y_to_dec(x // 10, y)


# Hex: 0123456789abcdef

def hex_filter(x):
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  'A', 'B', 'C', 'D', 'E', 'F']
    return characters[x]


def dec_to_hex(x):
    if x == 0:
        return '0'
    return dec_to_hex(x // 16) + hex_filter(x % 16)
