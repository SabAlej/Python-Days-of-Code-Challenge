"""
This module contains a program that calculates the area of a circle given its radius.
"""

import math

radius = input("Radius: ")

area = math.pi * float(radius) ** 2

print("Area: " + str(area))

