"""test for linter and formatter tools."""

import datetime as dt
import math


def print_test():
    """Test the print functionality."""
    print(math.cos(math.pi / 3))
    print("Hello" "World")
    print(dt.datetime.now())


print_test()
