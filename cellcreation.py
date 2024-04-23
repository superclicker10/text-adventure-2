from oobcreation import *
import random as r
import math as m
import time as t
class Cell:
    
    #temp = 20
    loot_max = 1        #default 1
    loot_chance = 100        # default 10
    id = "normal"

class Loot(Cell):
    
    loot = 1
    id = "loot"
    looted = False

class OOB(Cell):
    
    oob = True
    id = "oob"
    
cells = {}
def map_creation():
    print("Loading map...")
    oob_list = oob_creation_walls()     #adjust for all functions in oobcreation.py
    counter = 90601   # adjust for the amount of squares in the grid
    for x_co in range(-150, 151):         # adjust for (negative half of grid length, positive half of grid length+1) and these exclude 0 when talking about halves (the grid becomes 80x80)
        for y_co in range(150, -151, -1):         # adjust for same as above but opposite
            oob_cell = False
            temp_coords = (x_co, y_co)
            for temp in oob_list:
                if temp_coords == temp:
                    #print(temp_coords)
                    cells[f'({x_co}, {y_co})'] = OOB.id
                    #print(x_co, y_co)
                    oob_cell = True
            if r.randint(1, 100) <= Cell.loot_chance and oob_cell == False:
                cells[f'({x_co}, {y_co})'] = Loot.id
            elif oob_cell == False:
                cells[f'({x_co}, {y_co})'] = Cell.id
            counter -= 1
    cells[(0, 0)] = Cell.id
    return cells

"""  #preserving the pain i inflicted while making this whole conversion
def convert_coords(cells):   # checking algorithm to convert indexes in cells to coordinates
    for count in cells:
        x = (m.ceil((int(count))/20)) - 10
        y = -(int(count)%(m.ceil((int(count))/20)) - 10)
        print(x, y)
    temp = 22       # adjust for one plus the full length of the grid
    x = -11         # minimum x coordinate -1
    y = 10          # maximum y coordinate
    keys = list(cells.keys())
    for count in range(1, 442):         # adjust loop range for the amount of squares + 1
        temp -= 1
        if temp == 0:
            y -= 1          
            x = -11         # same as above
            temp = 21       # adjust for the full length of the grid
        x += 1
        #print(keys[-count], "=", (x, y))
        if (x, y) in oob_creation():
            print((x, y), "is out of bounds")
        elif cells[keys[-count]] == "loot":
            print((x, y), "is a loot cell")
        else:
            print((x, y), "is a normal cell")
        
"""

def print_coords():
    for key, value in cells.items():
        if cells[key] == "oob":
            print(key, "is an", value, "cell")
        else:
            print(key, "is a", value, "cell")
    
#print(map_creation())
#t.sleep(100)
"""
oob_list = oob_creation()
for x in oob_list:
    print(x)
t.sleep(1000)
"""
#cells = map_creation()
#convert_coords(cells)
#map_creation()
#print_coords()
#print("done")
