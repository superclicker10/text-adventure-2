import time as t 
import operator as o

rarity_names = ["minimum",
    "pitiful",
    "bad",
    "subpar",
    "normal",
    "good",
    "epic",
    "legendary",
    "perfect"]
loot = ["health potion", "mana potion", "gold", "book", "trash"]

class Inventory:
    inventory = {}
    size = 20
    item_max = 100

def add_item(item, rarity, n):
    item = item.lower()
    try:        # handles max item limit
        if Inventory.inventory[f'{rarity} {item}'] >= 100:
            print("You have reached the maximum possible amount of this item.")
            t.sleep(n)
        else:
            Inventory.inventory[f'{rarity} {item}'] += 1
            print(f'Added {rarity} {item} to your inventory.')
            t.sleep(n)
    except Exception:   # handles max inventory size, exception is for the item not existing
        if len(Inventory.inventory) > Inventory.size:
            print("You have reached the maximum inventory capacity.")
            t.sleep(n)
        else:
            Inventory.inventory[f'{rarity} {item}'] = 1
            print(f'Added {rarity} {item} to your inventory.')
            t.sleep(n)

def drop_item(item, rarity, n):
    rarity = input("Enter the rarity (pitiful, bad, subpar, normal, good, epic, legendary, perfect): ")
    if rarity not in rarity_names:
        print("That is not a valid rarity.")
        return 0
    item = input("Enter type of item (health potion, mana potion): ")       # update for future items
    if item not in loot:
        print("That is not a valid item.")
        return 0
    if f'{rarity.lower()} {item}' not in Inventory.inventory.keys():
        print("That item is not in your inventory.")
        return 0
    try:
        if Inventory.inventory[f'{rarity} {item}'] <= 0:
            print("You cannot drop that item.")
            t.sleep(n)
        else:
            Inventory.inventory[f'{rarity} {item}'] -= 1
            print(f'Removed {rarity} {item} to your inventory.')
            t.sleep(n)
            if Inventory.inventory[f'{rarity} {item}'] <= 0:
                Inventory.inventory.pop(f'{rarity} {item}')
                
    except Exception:
        print("You do not have that item.")
        t.sleep(n)

def print_inventory():
    #Inventory.inventory = dict(sorted(Inventory.inventory, key=o.itemgetter(0)))
    # i am not introducing sorting the inventory. ever.
    if Inventory.inventory == {}:
        print("Your inventory is empty.")
    for key in Inventory.inventory.keys():
        print(f'{key}: {Inventory.inventory[key]}')
    """
    print(Inventory.inventory)
    for item in Inventory.inventory:
        print(item)
    Inventory.inventory = dict(Inventory.inventory)
    """