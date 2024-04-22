#!/usr/bin/env python3
"""
A annotated function  which takes a list of integers and floats and returns their sum as a float.
"""


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Accepts a mixed list of integers and floats and returns their sum as a float.
    """
    result = 0.0
    for x in mxd_lst:
        result += x
    return result
