from oobcreation import *
import random as r
import secrets as s
import math as m
import time as t
class Cell:
    
    #temp = 20
    loot_max = 1        #default 1
    loot_chance = 10        # default 10
    id = "normal"
    visited = False

class Start(Cell):
    
    id = "start"
    
class Loot(Cell):
    
    loot = 1
    id = "loot"
    looted = False

class OOB(Cell):
    
    oob = True
    id = "oob"
    
class Forge(Cell):
    
    id = "forge"
    forge_unlocked = False
    
class Market(Cell):
    
    id = "market"
    buy_max = 1 # default 1, add upgrades later
    option_amt = 3 # default 3
    market_amt = 59 # default 60, 1 used for default gen (line 65)    
    
cells = {}
cells_visited = {}
def map_creation():
    print("Loading map...")
    temp_counter = 0    # used for generating markets
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
            if r.randint(0, 100) <= Cell.loot_chance and oob_cell == False:
                cells[f'({x_co}, {y_co})'] = Loot.id
            elif oob_cell == False:
                cells[f'({x_co}, {y_co})'] = Cell.id
            counter -= 1
            #print(counter)
    #print("Cells done")
    cells[f'{r.randint(-10, 10)}, {r.randint(-10, 10)}'] = Forge.id   #generates guaranteed market and forge
    #print("Forge done")
    cells[f'{r.randint(-10, 10)}, {r.randint(-10, 10)}'] = Market.id
    while temp_counter <= Market.market_amt:
        x_co = r.randint(-140, 140)
        y_co = r.randint(-140, 140)
        #print("Loop test")
        #print(cells[f'({x_co}, {y_co})'])
        if cells[f'({x_co}, {y_co})'] != Cell.id:
            continue
        elif cells[f'({x_co}, {y_co})'] == Cell.id:
            cells[f'({x_co}, {y_co})'] = Market.id
            temp_counter += 1
            #print(temp_counter)
    #print("Markets done")
    cells[f'({1}, {0})'] = Market.id
    cells[f'({0}, {0})'] = Start.id
    return cells

def visited_creation():
    for x_co in range(-150, 151):   
        for y_co in range(150, -151, -1): 
            cells_visited[f'({x_co}, {y_co})'] = False
    #print(cells_visited)

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