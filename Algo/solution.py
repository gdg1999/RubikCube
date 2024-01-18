# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:14:12 2023

@author: Gregory
"""

import time
import json
import os.path
from random import choice
from tqdm import tqdm
from Tools import cube, str2numpy
import copy


class IDA_star(object):
    def __init__(self, heuristic, cube, max_depth = 20):
        """
        Input: heuristic - dictionary representing the heuristic pre computed map
                max_depth - integer representing the max depth you want your game tree to reach (default = 20) [OPTIONAL]
        Description: Initialize the solver
        Output: None
        """
        self.max_depth = max_depth
        self.threshold = max_depth
        self.min_threshold = None
        self.heuristic = heuristic
        self.forCube = copy.deepcopy(cube)
        self.solution = ""

    def deal(self, state):
        """
        Input: state - string representing the current state of the cube
        Description: solve the rubix cube
        Output: list containing the moves taken to solve the cube
        """
        while True:
            status = self.search(state, 1)
            if status: return self.solution
            self.solution = ""
            self.threshold = self.min_threshold
        return ""


    def search(self, state, g_score):
        """
        Input: state - string representing the current state of the cube
                g_score - integer representing the cost to reach the current node
        Description: search the game tree using the IDA* algorithm
        Output: boolean representing if the cube has been solved
        """

        if self.forCube.check():
            return True
        elif len(self.solution)/2 >= self.threshold:
            return False
        
        min_val = float('inf')
        best_action = None
        
        actions = [D+A for D in ['F','R','D','B','L','U']
                       for A in ['1', '2', '3']]
        
        for a in actions:
            cube_temp = cube.Cube(3, str2numpy.transfer(state))
            cube_temp.twist(a[0], a[1])
                
            if cube_temp.check():
                self.solution = self.solution + a
                return True
            
            cube_str = cube_temp.stringfy()
            h_score = self.heuristic[cube_str] if cube_str in self.heuristic else self.max_depth
            f_score = g_score + h_score
            if f_score < min_val:
                min_val = f_score
                best_action = [(cube_str, a)]
            elif f_score == min_val:
                if best_action is None:
                    best_action = [(cube_str, a)]
                else:
                    best_action.append((cube_str, a))
        if best_action is not None:
            if self.min_threshold is None or min_val < self.min_threshold:
                self.min_threshold = min_val
            next_action = choice(best_action)
            self.solution = self.solution + next_action[1]
            status = self.search(next_action[0], g_score + min_val)
            if status: return status
        return False


def build_heuristic_table(state, actions, max_moves = 20, heuristic = None):
    """
    Input: state - string representing the current state of the cube
            actions -list containing tuples representing the possible actions that can be taken
            max_moves - integer representing the max amount of moves alowed (default = 20) [OPTIONAL]
            heuristic - dictionary containing current heuristic map (default = None) [OPTIONAL]
    Description: create a heuristic map for determining the best path for solving a rubiks cube
    Output: dictionary containing the heuristic map
    """
    if heuristic is None:
        heuristic = {state: 0}
    que = [(state, 0)]
    node_count = sum([len(actions) ** (x + 1) for x in range(max_moves + 1)])
    with tqdm(total=node_count, desc='Heuristic DB') as pbar:
        while True:
            if not que:
                break
            s, d = que.pop()
            if d > max_moves:
                continue
            for a in actions:
                cube_temp = cube.Cube(3, str2numpy.transfer(s))
                cube_temp.twist(a[0], a[1])
                a_str = cube_temp.stringfy()
                if a_str not in heuristic or heuristic[a_str] > d + 1:
                    heuristic[a_str] = d + 1
                que.append((a_str, d+1))
                pbar.update(1)
    return heuristic


def solve(cube):
    
    MAX_MOVES = 5
    NEW_HEURISTICS = False
    HEURISTIC_FILE = 'heuristic.json'
    inistate = copy.deepcopy(cube)
    inistate.reset()

    #--------------------------------

    if os.path.exists(HEURISTIC_FILE):
        with open(HEURISTIC_FILE) as f:
            table = json.load(f)
    else:
        table = None

    if table is None or NEW_HEURISTICS is True:
        actions = [D+A for D in ['F','R','D','B','L','U']
                       for A in ['1', '2', '3']]
        table = build_heuristic_table(
            inistate.stringfy(),
            actions,
            max_moves = MAX_MOVES,
            heuristic = table
        )

        with open(HEURISTIC_FILE, 'w', encoding='utf-8') as f:
            json.dump(
                table,
                f,
                ensure_ascii=False,
                indent=4
            )

    
    start_time = time.time()
    
    solver = IDA_star(table, cube)
    solution = solver.deal(cube.stringfy())
    
    end_time = time.time()
    solve_Time = end_time - start_time
    
    return solution, solve_Time