from cellcreation import *
from markets import *   #the error with imported files is false, it works just fine
from move import *
from lootgeneration import *
from inventory import *
from items import *
from forge import *
from filegen import *
import time as t

x = 0
y = 0
n = 1
choice = None
global_market_buffer = False
item_grabbed = False
grid = Grid()
inventory = Inventory()
no_rarity_list = ["gold", "scrap"]
loot = ["health potion", "mana potion", "gold", "book", "scrap"]
stat_items = [
    "max_health",
    "max_mana",
    "attack",
    "defence"
]

class Player:  # making health and mana exist, as well as their stats.
    def __init__(self):
        self.health = 100    # default 100
        self.max_health = 100    # default 100
        self.health_regen = 2    # default 2
        self.mana = 100   # default 100
        self.max_mana = 100  # default 100
        self.mana_regen = 0.2    # default 0.2
        self.attack = 1  # default 1
        self.defence = 0     # default 0

player = Player()

stats_list_name = ["health",
    "max health",
    "health regeneration",
    "mana",
    "max mana",
    "mana regeneration",
    "attack",
    "defence",
    "gold"
]

def update_stats_list():
    global stats_list
    try:
        stats_list = [player.health,    # reinitializing the list to update the values
            player.max_health,
            player.health_regen,
            player.mana,
            player.max_mana,
            player.mana_regen,
            player.attack,
            player.defence,
            Inventory.inventory["gold"]]
    except:
        stats_list = [player.health,    # reinitializing the list to update the values
            player.max_health,
            player.health_regen,
            player.mana,
            player.max_mana,
            player.mana_regen,
            player.attack,
            player.defence,
            0]
    #print("Updated stats_list:", stats_list)

update_stats_list()

rarity_names = ["minimum",
    "pitiful",
    "bad",
    "subpar",
    "normal",
    "good",
    "epic",
    "legendary",
    "perfect"]

requirements_file_write = [
    "pitiful: 2 items",
    "bad: 2 items",
    "subpar: 2 items",
    "normal: 2 items",
    "good: 2 items",
    "epic: 3 items",
    "legendary: 5 items",
    "perfect: 10 items",
    "\n",
    "Book rarities -",
    "blank: 2 items",
    "overrated: 2 items",   
    "bad: 2 items",
    "normal: 2 items",
    "knowledgeable: 2 items",
    "intellectual: 3 items",
    "philosophical: 5 items",
    "wisdom: 10 items"
]
    
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
    if player.health >= player.max_health:
        player.health = player.max_health
    else:
        player.health = round(player.health + player.health_regen, 2)
    if player.mana >= player.max_mana:
        player.mana = player.max_mana
    else:
        player.mana = round(player.mana + player.mana_regen, 2)
    if player.health >= player.max_health:  #double checks so health is always correct
        player.health = player.max_health
    if player.mana >= player.max_mana:
        player.mana = player.max_mana
    update_stats_list()

def stats():
    print("Your stats are: ", end="")
    print("\n")
    t.sleep(n)
    print(f'position: ({x}, {y})')
    update_stats_list()
    #print(stats_list)
    for pos in range(0, len(stats_list)):
        print(f'{stats_list_name[pos]}: {stats_list[pos]}')
    t.sleep(2)

def forge():
    if Forge.forge_unlocked == False:
        print("You can't do that.")
        t.sleep(n)
        return 0
    print("")
    item = input("What item do you want to merge? (only enter item name:) ").lower().strip()
    if item in no_rarity_list or item not in loot:  
        print("You can't merge that item.")
        t.sleep(n)
        return 0
    if item == "book":
        rarity = input("What rarity do you want to merge? (blank, overrated, bad, normal, knowledgeable, intellectual, philosophical, wisdom): ").lower().strip()
        if rarity not in book_rarity_names:
            print("That isn't a valid rarity.")
            t.sleep(n)
            return 0
    else:
        rarity = input("What rarity do you want to merge? (pitiful, bad, subpar, normal, good, epic, legendary, perfect): ").lower().strip()
        if rarity not in rarity_names:
            print("That isn't a valid rarity.")
            t.sleep(n)
            return 0
    if f'{rarity} {item}' not in Inventory.inventory:
        print("You don't have that item.")
        t.sleep(n)
        return 0
    if rarity == rarity_names[-1]:
        print("This is the max rarity, you cannot merge further.")  #maybe add another rarity only through merging?
        t.sleep(n)
        return 0
    try:
        amount = int(input("Enter the amount of merged item to produce (see requirements.txt for the amount needed to merge to next rarity): ")).strip()
    except:
        print("That isn't a valid amount.")
        t.sleep(n)
        return 0
    if amount <= 0:
        print("That isn't a valid amount.")
        t.sleep(n)
        return 0
    merge_items(item, rarity, amount, n)    

def market_intro(stats_list, n):
    global global_market_buffer
    global player
    while True:
        try:
            choice = input("Enter market or stay outside? (enter, stay): ").lower().strip()
        except:
            print("You can't do that.")
            t.sleep(n)
            continue
        if choice == "enter":
            try:
                choice = input("Buy or sell items? (buy, sell): ").lower().strip()
            except:
                print("You can't do that.")
                t.sleep(n)
                continue
            if choice == "buy":
                buy_options(Market.option_amt, n, stats_list) # print_options once made
                global_market_buffer = True
                break
            elif choice == "sell":
                sell_item(n)
                global_market_buffer = True
                break
            else:
                print("You can't do that.")
                t.sleep(n)
                continue
            global_market_buffer = True
        elif choice == "stay":
            print("Staying on the outside...")
            t.sleep(n)
            global_market_buffer = True
            break
        else:
            print("You can't do that.")
            t.sleep(n)
            continue

def normalize_stat_name(stat_name): #chatgpt lol
    return stat_name.replace(" ", "_").lower()

def stat_items_process(): #processes stat items from market
    temp = list(Inventory.inventory.keys())
    #print("Inventory before processing stat items:", temp)
    for item in temp:
        try:
            parts = item.split(" ")
            rarity = parts[0]
            stat_name = " ".join(parts[1:])
            
            normalized_stat_name = normalize_stat_name(stat_name)
            
            if normalized_stat_name in stat_items:
                increase = getattr(atk_def_misc, rarity)
                amount = getattr(player, normalized_stat_name)
                setattr(player, normalized_stat_name, amount + increase)
                #print(f"Updated stat: {normalized_stat_name} to {getattr(player, normalized_stat_name)}")
        except Exception as e:
            #print("Error processing item:", item, e)
            continue
    try:
        if item in stat_items:
            remove_item(rarity, stat_name)
    except Exception as e:
        #print("Error removing item:", e)
        pass
    update_stats_list()
    #print("Updated stats_list after processing:", stats_list)
    
def move():
    global x
    global y
    global global_market_buffer
    move_success = False
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
        move_success = True
    except Exception:
        print("You have entered an invalid movement direction.")
    if move_success == True:
        global_market_buffer = False
    return x, y

def use():
    use_item(player, n)

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
    global item_grabbed
    """
    for x in range(-150, 151):
        for y in range(-150, 151):
            if cells[f'({x}, {y})'] == Market.id:
                print(x, y)
    """
    if choice != "move" or global_market_buffer == True or item_grabbed == True:      # update for stopping farming of health and mana
        pass
    else:
        hp_and_mana_update()
    stat_items_process()
    #print(stats_list)
    item_grabbed = False
    if cells_visited[f'({x}, {y})'] == True:
        print(f'You are currently at ({x}, {y}) (already visited).')
    else:
        print(f'You are currently at ({x}, {y}).')
    t.sleep(n)
    cells_visited[f'({x}, {y})'] = True
    print(f'You have {player.health} health and {player.mana} mana.')
    t.sleep(n)
    if cells[f'({x}, {y})'] == "loot":          # checking for loot cells
        print("You landed on a loot cell!")
        t.sleep(n)
        loot_cell_intro(x, y, n)
        item_grabbed = True
        return 0
    if cells[f'({x}, {y})'] == "market":
        if global_market_buffer == True:
            pass
        else:
            print("You landed on a market!")
            t.sleep(n)
            market_intro(stats_list, n) #double regen is intentional
            return 0
    if cells[f'({x}, {y})'] == "forge":
        if Forge.forge_unlocked == False:
            print("You landed at the forge!")
            t.sleep(n)
            print("You can now use the forge anywhere to merge items.")
            t.sleep(n)
            make_reqs(requirements_file_write, n)
            Forge.forge_unlocked = True
            return 0
        else:
            choice = input("What would you like to do? (move, interact, use, forge, inventory, stats, exit): ").lower().strip()
    elif Forge.forge_unlocked == True:
        choice = input("What would you like to do? (move, interact, use, forge, inventory, stats, exit): ").lower().strip()
    else:
        choice = input("What would you like to do? (move, interact, use, inventory, stats, exit): ").lower().strip()
        #print(cells[(1, 0)], x, y)
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
    t1 = t.time()
    generate_map()
    visited_creation()
    t2 = t.time()
    print(f'Loading took {m.floor(t2-t1)} seconds')
    t.sleep(n)
    print("")
    while True:
        repeated_action()
        update_stats_list()
        print("\n", end="")
    



    
