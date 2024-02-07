"""functions"""
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