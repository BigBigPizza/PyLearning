# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:58:42 2026

@author: Chris
"""

directions1 = ["right 5", "up 2", "left 3", "down 1"]
directions2 = ["rig 5", "up 2", "left 3", "down 1"]

def find_treasure(directions):
    final_coord = [0,0]
    
    direction_key ={
        "left" : (-1,0),
        "right" : (1,0),
        "up" : (0,1),
        "down" : (0,-1),
        }
    
    for pair in directions:
        cardinal, vector = pair.split()
        if cardinal in direction_key:
            final_coord[0] += direction_key[cardinal][0] * int(vector)
            final_coord[1] += direction_key[cardinal][1] * int(vector)
        else:
            print(f"Invalid direction '{cardinal}' in '{pair}' this directions has been skipped")
    return final_coord
        
        
        
print(find_treasure(directions1))
print(find_treasure(directions2))