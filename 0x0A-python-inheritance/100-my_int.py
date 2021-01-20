#!/usr/bin/python3
""" my_int"""


class MyInt(int):
    """Class MyInt"""
    def __init__(self, xd):
        """iniciar"""
        self.xd = xd

    def __eq__(self, xd):
        return self.xd != xd

    def __ne__(self, xd):
        return self.xd == xd
