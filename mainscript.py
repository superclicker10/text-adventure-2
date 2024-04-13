from cellcreation import *
from move import *
from lootgeneration import *
from inventory import *
import time as t
x = 0
y = 0
n = 1
grid = Grid()
inventory = Inventory()
def delay():
    global n
    try:
        n = float(input("How long should the text delay be in seconds? (0.5-2): "))
    except:
        print("You have entered an invalid value. Delay set to default (1).")
        n = 1 
    if n < 0.5:
        print("Delay set to minimum value (0.5).")
        n = 0.5
    if n > 2:
        print("Delay set to maximum value (2).")
        n = 2

def generate_map():
    map_creation()

def move():
    global x
    global y
    direction = input("Where would you like to move? (left, right, up, down): ")
    try:
        temp_x = x
        temp_y = y
        try:
            x = eval(f'grid.{direction}(grid.oob_walls, temp_x, temp_y, n)')[0]     #update parameters should functions change
        except:
            return x, y
        if f'grid.{direction}(grid.oob_walls, temp_x, temp_y, n)' == False:
            return x, y
        y = eval(f'grid.{direction}(grid.oob_walls, temp_x, temp_y, n)')[1]
    except Exception:
        print("You have entered an invalid movement direction.")
    return x, y

def inventory():
    choice = input("View or drop item?: ")
    if choice == "view":
        print("Here is your inventory: ", "\n")
        t.sleep(n)
        print_inventory()
    elif choice == "drop":
        item = rarity = None
        try:
            amount = int(input("Enter the amount to drop: "))
            drop_item(item, rarity, amount, n)
        except Exception or amount <= 0:
            print("You have not entered a valid amount.")
            t.sleep(n)

def repeated_action():
    print(f'You are currently at ({x}, {y}).')
    if cells[f'({x}, {y})'] == "loot":          # checking for loot cells
        print("You landed on a loot cell!")
        t.sleep(n)
        loot_cell_intro(x, y, n)
        return 0
    choice = input("What would you like to do? (move, interact, use, inventory, exit): ")
    if choice == "exit":
        print("Thanks for playing!")
        t.sleep(1)
        exit()
    try:
        eval(f'{choice}()')
    except:
        print("You can't do that.")
        t.sleep(n)

if __name__ == "__main__":
    delay()
    print("\n", end="")
    generate_map()
    while True:
        repeated_action()
        print("\n", end="")



    
