import time as t
from oobcreation import *
class Grid:
    oob_walls = oob_creation_walls()          #adjust for all functions in oob_creation.py

    def right(self, oob_walls, x, y, n):
        if f'({x+1}, {y})' in oob_walls:
            print("You can't go any further.")
            t.sleep(n)
            return False
        else:
            x += 1
        t.sleep(n/2)
        return x, y
    
    def left(self, oob_walls, x, y, n):
        if f'({x-1}, {y})' in oob_walls:
            print("You can't go any further.")
            t.sleep(n)
            return False
        else:
            x -= 1
        t.sleep(n/2)
        return x, y

    def up(self, oob_walls, x, y, n):
        if f'({x}, {y+1})' in oob_walls:
            print("You can't go any further.")
            t.sleep(n)
            return False
        else:
            y += 1
        t.sleep(n/2)
        return x, y
    
    def down(self, oob_walls, x, y, n):
        if f'({x}, {y-1})' in oob_walls:
            print("You can't go any further.")
            t.sleep(n)
            return False
        else:
            y -= 1
        t.sleep(n/2)
        return x, y