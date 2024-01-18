# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:20:01 2023

@author: Gregory
"""

"""
How to model a Magic Cube?
And how to solve it?

The first thing we should do is to model our toy

Q1. Choose a proper perspective to represent your toy
A: using 2D plane with facelet,
   with F(red),R(blue),D(yellow),B(orange),L(green),U(white) 6 facelet fixed,
   and spread over in order;
   
   
Q2. Define each move you perform
A: only six direction moves and each of them with three kinds angle
   noted as U1L2R3, with clockwise circle 90 in U and 180 in L and 270 in R
   so maybe a procedure can be noted as: U1D2F2B3...L1R1.
   all of them we called permuter, 18 in total.


Q3: How to measure the extent of the chaos
A: using the shuffle times

"""


from Tools import performer, shuffle, cube, str2numpy
from Algo import solution


if __name__ == '__main__':

    shuffle_times = 11
    # user_defined = "L1B3D1R3B3F1D2U1F1R2U1"
    user_defined = None
    Original, ini_String = shuffle.shuffle(shuffle_times, user_defined)
    cube1 = cube.Cube(3, Original)
    Shuffle_times1 = performer.perform(cube1, ini_String)
    
    strategy1, solveTime = solution.solve(cube1)
    
    total_times1 = performer.perform(cube1, strategy1)
    twist_times = total_times1 - Shuffle_times1
    
    print(f"solveTime is {solveTime:.3f}\n")
    print(f"Shuffle_times are {Shuffle_times1}\n")
    print(f"twist_times are {twist_times}\n")
    
    
    my_cube = "rrgrrrwrrybbwbbbbbyyyyyyyybcccccccccggggggggrwwwwwwwbr"
    data = str2numpy.transfer(my_cube)
    cube2 = cube.Cube(3, data)
    cube2.visualizer()
    strategy2, solveTime2 = solution.solve(cube2)
    total_times2 = performer.perform(cube2, strategy2)
    
    print(f"solveTime is {solveTime:.3f}\n")
    print(f"twist_times are {total_times2}\n")
    

