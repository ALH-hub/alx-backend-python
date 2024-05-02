#!/usr/bin/env python3
"""Type-annotated function zoom_array that takes a tuple lst as argument"""
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """Return a tuple of tuples"""
    zoomed_in: Tuple = tuple(item for item in lst
                             for i in range(factor))
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3.0)
