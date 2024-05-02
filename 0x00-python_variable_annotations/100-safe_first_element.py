#!/usr/bin/env python3
"""Type-annotated function safe_first_element
that takes a sequence input_list of any type
and returns its first element if exists, otherwise None.
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst if exists, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
