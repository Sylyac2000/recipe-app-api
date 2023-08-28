"""Calculators functions"""


def add(x, y):
    """sum x, and y and return result"""
    return x + y


def substract(x, y):
    """Substract y to x """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or
            isinstance(y, float)):
        return x - y

    return ValueError()
