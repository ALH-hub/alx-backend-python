#!/usr/bin/env python3
"""Type-annotated function zoom_array that takes a Tuple lst"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list of zoomed-in elements"""
    zoomed_in: List = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
