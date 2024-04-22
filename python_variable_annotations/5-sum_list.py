#!/usr/bin/env python3
"""
A annonitation function that takes a input of list.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up the float values in the input list.
    """
    return sum(input_list)
