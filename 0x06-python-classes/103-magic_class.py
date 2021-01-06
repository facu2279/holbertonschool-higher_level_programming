#!/usr/bin/python3
"""class MagicClass"""

import math


class MagicClass:
    """class MagicClass"""

    def __init__(self, radius=0):
        """class MagicClass"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """class MagicClass"""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """class MagicClass"""
        return 2 * math.pi * self._MagicClass__radius
