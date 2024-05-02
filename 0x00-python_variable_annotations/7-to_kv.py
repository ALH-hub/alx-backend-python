#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string k and an int OR float v"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and v"""
    return (k, v**2)
