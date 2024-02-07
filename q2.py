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

# --- Code Beyond this point just for fun, so some are left unfinished ---

# Hex: 0123456789abcdef

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  'A', 'B', 'C', 'D', 'E', 'F']

def hex_filter(x):
    return characters[x]

def hex_revert(x, lst):
    if x == lst[0]:
        return 0
    return 1 + hex_revert(x, lst[1:])

def dec_to_hex(x):
    if x < 16:
        return hex_filter(x)
    return dec_to_hex(x // 16) + hex_filter(x % 16)

def hex_to_dec(x):
    if len(x) == 1:
        return hex_revert(x,characters)
    return hex_revert(x[-1], characters) + 16 * hex_to_dec(x[:-1])

# # complement system
# def is_negative(x,y):
#     """input non-decimal numbers
#     :param x: int, str
#     :param y: int
#     :return bool
#     """
#     if y > 10:
#         # code
#     # code for base < 10

# def bin_complement(x):
#     """return negative value equivalent in 2's complement system"""
#
# def base_y_complement(x,y):
#     """return negative value equivalent in y's complement system"""
#
# def hex_complement(x):
#     """return negative value equivalent in Hexadecimal complement system"""

# def bit16(x,y):
#     """take input and turn it into 16 bit"""
#     if