# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:57:23 2023

@author: Gregory
"""

"""
This is a cube
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use( ['science',"grid","ieee"])
import copy


def rotate_matrix(matrix, rotations):
    
    m, n = len(matrix), len(matrix[0])
    rotated = []

    if rotations == 1:
        rotated = [[matrix[i][j] for i in range(m - 1, -1, -1)] for j in range(n)]
    elif rotations == 2:
        rotated = [[matrix[i][j] for j in range(n - 1, -1, -1)] for i in range(m - 1, -1, -1)]
    elif rotations == 3:
        rotated = [[matrix[i][j] for i in range(m)] for j in range(n - 1, -1, -1)]
    else:
        print("only for 90, 180, 270 rotation.")
    
    numpy_array = np.array(rotated)

    return numpy_array


class Cube(object):
    """
    The class of the cubic
    """
    Cube_num = 0
    FaceColor = {'F':'r','R':'b','D':'y','B':'c','L':'g','U':'w'}
    Faceindex = { 1 :'F', 2 :'R', 3 :'D', 4 :'B', 5 :'L', 6 :'U'}

    
    def __init__(self, n, ini_state):
        self.count = 0
        self.n = n
        self.ini_state = copy.deepcopy(ini_state)
        self.state = copy.deepcopy(ini_state)
        self.pre_state = copy.deepcopy(ini_state)
        self.counter = 0
        Cube.Cube_num += 1
    
    
    def twist(self, direction, angle):
        if direction == 'F':
            if angle == '1':
                self.state[:,:,0] = rotate_matrix(self.pre_state[:,:,0], int(angle))  # Front
                self.state[:,0,1] = self.pre_state[2,:,5]  # Right
                self.state[2,:,2] = self.pre_state[:,0,1]  # Down
                self.state[:,2,4] = self.pre_state[2,:,2]  # Left
                self.state[2,:,5] = self.pre_state[:,2,4]  # Upper
                
            elif angle == '2':
                self.state[:,:,0] = rotate_matrix(self.pre_state[:,:,0], int(angle))  # Front
                self.state[:,0,1] = self.pre_state[:,2,4]  # Right
                self.state[2,:,2] = self.pre_state[2,:,5]  # Down
                self.state[:,2,4] = self.pre_state[:,0,1]  # Left
                self.state[2,:,5] = self.pre_state[2,:,2]  # Upper
                
            elif angle == '3':
                self.state[:,:,0] = rotate_matrix(self.pre_state[:,:,0], int(angle))  # Front
                self.state[:,0,1] = self.pre_state[2,:,2]  # Right
                self.state[2,:,2] = self.pre_state[:,2,4]  # Down
                self.state[:,2,4] = self.pre_state[2,:,5]  # Left
                self.state[2,:,5] = self.pre_state[:,0,1]  # Upper
                
            else:
                print("Wrong Twist, angle should be int and in [1,3]")
        
        elif direction == 'R':
            if angle == '1':
                self.state[:,:,1] = rotate_matrix(self.pre_state[:,:,1], int(angle))  # Right
                self.state[:,2,0] = self.pre_state[:,0,2]  # Front
                self.state[:,0,2] = self.pre_state[0,:,3]  # Down
                self.state[0,:,3] = self.pre_state[:,2,5]  # Behind
                self.state[:,2,5] = self.pre_state[:,2,0]  # Upper
                
            elif angle == '2':
                self.state[:,:,1] = rotate_matrix(self.pre_state[:,:,1], int(angle))  # Right
                self.state[:,2,0] = self.pre_state[0,:,3]  # Front
                self.state[:,0,2] = self.pre_state[:,2,5]  # Down
                self.state[0,:,3] = self.pre_state[:,2,0]  # Behind
                self.state[:,2,5] = self.pre_state[:,0,2]  # Upper
                
            elif angle == '3':
                self.state[:,:,1] = rotate_matrix(self.pre_state[:,:,1], int(angle))  # Right
                self.state[:,2,0] = self.pre_state[:,2,5]  # Front
                self.state[:,0,2] = self.pre_state[:,2,0]  # Down
                self.state[0,:,3] = self.pre_state[:,0,2]  # Behind
                self.state[:,2,5] = self.pre_state[0,:,3]  # Upper
                
            else:
                print("Wrong Twist, angle should be int and in [1,3]")
              
        elif direction == 'D':
            if angle == '1':
                self.state[:,:,2] = rotate_matrix(self.pre_state[:,:,2], int(angle))  # Down
                self.state[2,:,0] = self.pre_state[2,:,4]  # Front
                self.state[2,:,1] = self.pre_state[2,:,0]  # Right
                self.state[:,0,3] = self.pre_state[2,:,1]  # Behind
                self.state[2,:,4] = self.pre_state[:,0,3]  # Left
                
            elif angle == '2':
                self.state[:,:,2] = rotate_matrix(self.pre_state[:,:,2], int(angle))  # Down
                self.state[2,:,0] = self.pre_state[:,0,3]  # Front
                self.state[2,:,1] = self.pre_state[2,:,4]  # Right
                self.state[:,0,3] = self.pre_state[2,:,0]  # Behind
                self.state[2,:,4] = self.pre_state[2,:,1]  # Left
                
            elif angle == '3':
                self.state[:,:,2] = rotate_matrix(self.pre_state[:,:,2], int(angle))  # Down
                self.state[2,:,0] = self.pre_state[2,:,1]  # Front
                self.state[2,:,1] = self.pre_state[:,0,3]  # Right
                self.state[:,0,3] = self.pre_state[2,:,4]  # Behind
                self.state[2,:,4] = self.pre_state[2,:,0]  # Left
                
            else:
                print("Wrong Twist, angle should be int and in [1,3]")
                  
        elif direction == 'B':
            if angle == '1':
                self.state[:,:,3] = rotate_matrix(self.pre_state[:,:,3], int(angle))  # Behind
                self.state[:,2,1] = self.pre_state[0,:,2]  # Right
                self.state[0,:,2] = self.pre_state[:,0,4]  # Down
                self.state[:,0,4] = self.pre_state[0,:,5]  # Left
                self.state[0,:,5] = self.pre_state[:,2,1]  # Upper
                
            elif angle == '2':
                self.state[:,:,3] = rotate_matrix(self.pre_state[:,:,3], int(angle))  # Down
                self.state[:,2,1] = self.pre_state[:,0,4]  # Right
                self.state[0,:,2] = self.pre_state[0,:,5]  # Down
                self.state[:,0,4] = self.pre_state[:,2,1]  # Left
                self.state[0,:,5] = self.pre_state[0,:,2]  # Upper
                
            elif angle == '3':
                self.state[:,:,3] = rotate_matrix(self.pre_state[:,:,3], int(angle))  # Down
                self.state[:,2,1] = self.pre_state[0,:,5]  # Right
                self.state[0,:,2] = self.pre_state[:,2,1]  # Down
                self.state[:,0,4] = self.pre_state[0,:,2]  # Left
                self.state[0,:,5] = self.pre_state[:,0,4]  # Upper
                
            else:
                print("Wrong Twist, angle should be int and in [1,3]")
            
        elif direction == 'L':
            if angle == '1':
                self.state[:,:,4] = rotate_matrix(self.pre_state[:,:,4], int(angle))  # Left
                self.state[:,0,0] = self.pre_state[:,0,5]  # Front
                self.state[:,2,2] = self.pre_state[:,0,0][::-1]  # Down
                self.state[2,:,3] = self.pre_state[:,2,2][::-1]  # Behind
                self.state[:,0,5] = self.pre_state[2,:,3]  # Upper
                
            elif angle == '2':
                self.state[:,:,4] = rotate_matrix(self.pre_state[:,:,4], int(angle))  # Down
                self.state[:,0,0] = self.pre_state[2,:,3]  # Right
                self.state[:,2,2] = self.pre_state[:,0,5]  # Down
                self.state[2,:,3] = self.pre_state[:,0,0]  # Left
                self.state[:,0,5] = self.pre_state[:,2,2]  # Upper
                
            elif angle == '3':
                self.state[:,:,4] = rotate_matrix(self.pre_state[:,:,4], int(angle))  # Down
                self.state[:,0,0] = self.pre_state[:,2,2][::-1]  # Right
                self.state[:,2,2] = self.pre_state[2,:,3][::-1]  # Down
                self.state[2,:,3] = self.pre_state[:,0,5]  # Left
                self.state[:,0,5] = self.pre_state[:,0,0]  # Upper
                
            else:
                print("Wrong Twist, angle should be int and in [1,3]")    

        elif direction == 'U':
            if angle == '1':
                self.state[:,:,5] = rotate_matrix(self.pre_state[:,:,5], int(angle))  # Upper
                self.state[0,:,0] = self.pre_state[0,:,1]  # Front
                self.state[0,:,1] = self.pre_state[:,2,3]  # Right
                self.state[:,2,3] = self.pre_state[0,:,4]  # Behind
                self.state[0,:,4] = self.pre_state[0,:,0]  # Left
                
            elif angle == '2':
                self.state[:,:,5] = rotate_matrix(self.pre_state[:,:,5], int(angle))  # Down
                self.state[0,:,0] = self.pre_state[:,2,3]  # Front
                self.state[0,:,1] = self.pre_state[0,:,4]  # Right
                self.state[:,2,3] = self.pre_state[0,:,0]  # Behind
                self.state[0,:,4] = self.pre_state[0,:,1]  # Left
                
            elif angle == '3':
                self.state[:,:,5] = rotate_matrix(self.pre_state[:,:,5], int(angle))  # Down
                self.state[0,:,0] = self.pre_state[0,:,4]  # Front
                self.state[0,:,1] = self.pre_state[0,:,0]  # Right
                self.state[:,2,3] = self.pre_state[0,:,1]  # Behind
                self.state[0,:,4] = self.pre_state[:,2,3]  # Left
                
            else:
                print("Wrong Twist, angle should be int and in [1,3]")
        
        else:
            print("Wrong Directions")
            
        self.pre_state = copy.deepcopy(self.state)
        self.counter += 1

        
    def visualizer(self):
        
        fig, ax = plt.subplots(figsize=(9, 1.5))
        
        ax.set_xlim(0, 20)
        ax.set_ylim(0, 3)
        ax.set_xticks([])
        ax.set_yticks([])

       
        for i in range(6):
            row = i // 6  
            col = i % 6   
            square_size = 2.4  
            
            
            square = plt.Rectangle((col * (square_size + 1), row * (square_size + 1)), square_size, square_size, fill=False, color='black', linewidth=2)
            ax.add_patch(square)
            
            
            for j in range(9):
                sub_row = j // 3  
                sub_col = j % 3   
                sub_square_size = 1  
                co = Cube.FaceColor[Cube.Faceindex[self.state[sub_row, sub_col, i]]]
                sub_square = plt.Rectangle((col * (square_size + 1) + sub_col * sub_square_size,
                                            row * (square_size + 1) + (2-sub_row) * sub_square_size),
                                           sub_square_size-0.09, sub_square_size-0.09,
                                           color=co)
                ax.add_patch(sub_square)
                ax.set_aspect('equal', adjustable='box')
                
        plt.show()

    
    def check(self):
        Check = False
        index = 0
        for face in range(self.state.shape[2]):
            python_nested_list = self.state[:,:,face].tolist()
            my_set = set()
            for row in python_nested_list:
                for element in row:
                    my_set.add(element)
            
            if len(my_set) == 1:
                index += 1
        
        if index == 6:
            Check = True
        
        return Check
    
    
    def reset(self):
        Facelet = np.ones([3,3,6])
        for index in range(Facelet.shape[2]):
            Facelet[:,:,index] = index + 1
            
        self.state = copy.deepcopy(Facelet)
        self.ini_state = copy.deepcopy(Facelet)
        self.pre_state = copy.deepcopy(Facelet)
        
    
    def stringfy(self):
        state_string = ""
        for num in range(self.state.shape[2]):
            for row in range(self.n):
                for col in range(self.n):
                    color = Cube.FaceColor[Cube.Faceindex[self.state[row, col, num]]]
                    state_string = state_string + color
        
        return state_string

 
    
    
    
    
    
    
    