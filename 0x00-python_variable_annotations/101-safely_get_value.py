#!/usr/bin/env python3
"""Type-annotated function safely_get_value
that takes a dict input_dict, a key key, a default value
default=None and returns the value with the specified key.
"""
from typing import Union, Any, Mapping


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[Any, None] = None) -> Union[Any, None]:
    """Return the value with the specified key if exists, otherwise None"""
    if key in dct:
        return dct[key]
    else:
        return default
