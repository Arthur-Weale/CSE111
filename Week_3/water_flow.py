"""
==========================================
    Program: Water flow
    Author: Arthur Weale
    Date: 1-15-2025
    Description:
        A Python program that generates simple English sentences.
==========================================
"""

import pytest
from pytest import approx

def water_column_height(tower_height, tank_height):
    water_height = tower_height + (3 * tank_height / 4)