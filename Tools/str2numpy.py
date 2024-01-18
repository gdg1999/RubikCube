# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:48:08 2023

@author: 29639
"""

import numpy as np

def transfer(stringfy):
    
    ColorNum = {'r':1, 'b':2, 'y':3, 'c':4, 'g':5, 'w':6}

    numeric_list = [ColorNum[char] for char in stringfy if char in ColorNum]

    grouped_lists = [numeric_list[i:i+9] for i in range(0, len(numeric_list), 9)]

    matrices = [np.array(grouped_list).reshape(3, 3) for grouped_list in grouped_lists]
    
    ini_state = np.stack(matrices, axis=2)

    
    return ini_state
    