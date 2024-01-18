# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:29:52 2023

@author: Gregory
"""

import numpy as np
import random


def shuffle(shuffle_times, user_defined):
    """
    Randomly generating the shuffle string from list
    """
    
    
    Facelet = np.ones([3,3,6])
    for index in range(Facelet.shape[2]):
        Facelet[:,:,index] = index + 1
    
    if user_defined != None:
        return Facelet, user_defined
    
    
    Direction = ['F', 'R', 'D', 'B', 'L', 'U']
    Angle = [1, 2, 3]
    String = ''

    num_selections = shuffle_times  

    random_combinations = []
    for _ in range(num_selections):
        random_direction = random.choice(Direction)
        random_angle = random.choice(Angle)
        random_combinations.append(f"{random_direction}{random_angle}")
    

    for combination in random_combinations:
        String = String  + combination
    

    return Facelet, String