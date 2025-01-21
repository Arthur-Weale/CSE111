"""
==========================================
    Program: Water flow
    Author: Arthur Weale
    Date: 1-15-2025
    Description:
        A Python Test Driven Development assignment.
==========================================
"""

import pytest

def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height):
    return (998.2 * 9.80665 * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    return (-friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)