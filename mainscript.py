from cellcreation import *
from move import *
from lootgeneration import *
from inventory import *
from items import *
from forge import *
import time as t
x = 0
y = 0
n = 1
choice = None
grid = Grid()
inventory = Inventory()
no_rarity_list = ["gold", "scrap"]

class Player:       #making health and mana exist, as well as their stats.                          
    health = 100    #default 100
    max_health = 100    #default 100
    health_regen = 2    #default 2
    mana = 100   #default 100
    max_mana = 100  #default 100
    mana_regen = 0.2    #default 0.2

stats_list = [Player.health,
    Player.max_health,
    Player.health_regen,
    Player.mana,
    Player.max_mana,
    Player.mana_regen]

stats_list_name = ["health",
    "max health",
    "health regeneration",
    "mana",
    "max mana",
    "mana regeneration"
]

rarity_names = ["minimum",
    "pitiful",
    "bad",
    "subpar",
    "normal",
    "good",
    "epic",
    "legendary",
    "perfect"]

requirements = {
    "minimum": 2,
    "pitiful": 2,
    "bad": 2,
    "subpar": 2,
    "normal": 2,
    "good": 2,
    "epic": 3,
    "legendary": 5,
    "perfect": 10
}
    
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

def hp_and_mana_update():
    if Player.health >= Player.max_health:
        Player.health = Player.max_health
        pass
    else:
        Player.health = round(Player.health + Player.health_regen, 2)
    if Player.mana >= Player.max_mana:
        Player.mana = Player.max_mana
        pass
    else:
        Player.mana = round(Player.mana + Player.mana_regen, 2)

def stats():
    print("Your stats are: ", end="")
    print("\n")
    t.sleep(n)
    print(f'position: ({x}, {y})')
    stats_list = [Player.health,    #reinitializing the list to update the values
    Player.max_health,
    Player.health_regen,
    Player.mana,
    Player.max_mana,
    Player.mana_regen]
    for pos in range(0, len(stats_list)):
        print(f'{stats_list_name[pos]}: {stats_list[pos]}')
    t.sleep(2)

def forge():
    item = input("What item do you want to merge? (only enter item name:) ").lower().strip()
    if item in no_rarity_list:  
        print("You can't merge that item.")
        t.sleep(n)
        return 0
    if item == "book":
        print("You can't merge books yet. (coming in a future update)")
        return 0
        """
        rarity = input("What rarity do you want to merge? (blank, overrated, bad, normal, knowledgeable, intellectual, philosophical, wisdom): ").lower().strip()
        if rarity not in book_rarity_names:
            print("That isn't a valid rarity.")
            t.sleep(n)
            return 0
        """
    else:
        rarity = input("What rarity do you want to merge? (pitiful, bad, subpar, normal, good, epic, legendary, perfect): ").lower().strip()
        if rarity not in rarity_names:
            print("That isn't a valid rarity.")
            t.sleep(n)
            return 0
    if rarity not in rarity_names:  #add book merging for this
        print("That isn't a valid rarity.")
        t.sleep(n)
        return 0
    elif f'{rarity} {item}' not in Inventory.inventory:
        print("You don't have that item.")
        t.sleep(n)
        return 0
    if rarity == rarity_names[-1]:
        print("This is the max rarity, you cannot merge further.")  #maybe add another rarity only through merging?
        t.sleep(n)
        return 0
    try:
        amount = int(input("Enter the amount of merged item to produce (see requirements.txt for the amount needed to merge to next rarity): "))
    except:
        print("That isn't a valid amount.")
        t.sleep(n)
        return 0
    if amount <= 0:
        print("That isn't a valid amount.")
        t.sleep(n)
        return 0
    merge_items(item, rarity, amount, n)    

def move():
    global x
    global y
    direction = input("Where would you like to move? (left, right, up, down): ").lower().strip()
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

def use():
    use_item(Player, n)

def inventory():
    choice = input("View or drop item? (view/drop): ").lower().strip()
    if choice == "view":
        print("Here is your inventory: ", "\n")
        t.sleep(n)
        print_inventory()
    elif choice == "drop":
        item = rarity = None
        try:
            amount = int(input("Enter the amount to drop: ")).lower().strip()
            drop_item(item, rarity, amount, n)
        except Exception or amount <= 0:
            print("You have not entered a valid amount.")
            t.sleep(n)
            
def repeated_action():
    global choice
    if choice != "move":      # update for stopping farming of health and mana
        pass
    else:
        hp_and_mana_update()
    print(f'You are currently at ({x}, {y}).')
    t.sleep(n)
    print(f'You have {Player.health} health and {Player.mana} mana.')
    t.sleep(n)
    if cells[f'({x}, {y})'] == "loot":          # checking for loot cells
        print("You landed on a loot cell!")
        t.sleep(n)
        loot_cell_intro(x, y, n)
        return 0
    choice = input("What would you like to do? (move, interact, use, forge, inventory, stats, exit): ").lower().strip()
    if choice == "exit":
        print("Thanks for playing!")
        t.sleep(1)
        exit()
    #try:
    eval(f'{choice}()')
    #except:
        #print("You can't do that.")
        #t.sleep(n)

if __name__ == "__main__":
    delay()
    print("\n", end="")
    generate_map()
    while True:
        repeated_action()
        print("\n", end="")



    
