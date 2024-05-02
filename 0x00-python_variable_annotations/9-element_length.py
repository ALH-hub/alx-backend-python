#!/usr/bin/env python3
"""Type-annotated function element_length
takes a list input_list of strings as argument"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples
    each tuple's first element is an element of lst
    and the second element is the length of the element.
    """
    return [(i, len(i)) for i in lst]
