# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:37:13 2023

@author: Gregory
"""

def perform(cube, strategy):
    """
    twist the cube you have
    """

    group_size = 2

    for i in range(0, len(strategy), group_size):
        group = strategy[i : i + group_size]
        cube.twist(group[0], group[1])
        cube.visualizer()
        print(f"Now you twist {cube.counter} times")
    
    
    return cube.counter