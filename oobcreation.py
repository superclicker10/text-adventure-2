"""
def oob_creation():
    oob = [
        (-7, 4), (-6, 4), 
        (-5, 4), (-4, 4), 
        (-3, 4), (-1, 4), 
        (-8, 3), (-2, 3), 
        (0, 3), (-8, 2), 
        (-6, 2), (-5, 2), 
        (-4, 2), (1, 2), 
        (-8, 1), (-6, 1), 
        (-5, 1), (-4, 1), 
        (1, 1), (-8, 0), 
        (-6, 0), (-5, 0), 
        (-4, 0), (-2, 0), 
        (2, 0), (-8, -1), 
        (-2, -1), (-1, -1), 
        (1, -1), (-7, -2), 
        (-6, -2), (-5, -2), 
        (-4, -2), (-3, -2), 
        (0, -2)
    ]
    return oob
"""
def oob_creation_walls(): 
    oob_walls = [f'({x}, 51)' for x in range(-50, 51)]   #adjust values for max y coords+1, max y coords, max y coords+1
    oob_walls.extend(f'({x}, -51)' for x in range(-50, 51))
    oob_walls.extend(f'(-51, {y})' for y in range(-50, 51))   #adjust values for max x coords+1, max x coords, max x coords+1
    oob_walls.extend(f'(51, {y})' for y in range(-50, 51))
    return oob_walls
    
print(oob_creation_walls())