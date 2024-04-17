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
loot = ["health potion", "mana potion", "gold", "book", "scrap"]

class Inventory:
    inventory = {}
    size = 30               #default 20 (adjust sizes in future updates.)
    item_max = 100             #default 100
    gold_max = 500

no_rarity = ["gold", "scrap"]
def add_item(item, rarity, amount, n):
    try:
        rarity = rarity.lower()
    except Exception:
        pass
    item = item.lower()
    if item not in no_rarity:
        try:        # handles max item limit
            if Inventory.inventory[f'{rarity} {item}'] >= Inventory.item_max:
                print("You have reached the maximum possible amount of this item.")
                Inventory.inventory[f'{rarity} {item}'] = Inventory.item_max
                t.sleep(n)
                return 0
            else:
                Inventory.inventory[f'{rarity} {item}'] += amount
                print(f'Added {amount} {rarity} {item} to your inventory.')
                t.sleep(n)
        except Exception:   # handles max inventory size, exception is for the item not existing
            if len(Inventory.inventory) > Inventory.size:
                print("You have reached the maximum inventory capacity.")
                t.sleep(n)
                return 0
            else:
                Inventory.inventory[f'{rarity} {item}'] = amount
                print(f'Added {amount} {rarity} {item} to your inventory.')
                t.sleep(n)
    else:
        try:        # handles max item limit
            if item == "gold" and Inventory.inventory["gold"] >= Inventory.gold_max:
                print("You have reached the maximum amount of this item.")
            elif Inventory.inventory[f'{item}'] >= Inventory.item_max:
                print("You have reached the maximum possible amount of this item.")
                Inventory.inventory[f'{item}'] = Inventory.item_max
                t.sleep(n)
                return 0
            else:
                Inventory.inventory[f'{item}'] += amount
                print(f'Added {amount} {item} to your inventory.')
                t.sleep(n)
        except Exception:   # handles max inventory size, exception is for the item not existing
            if len(Inventory.inventory) > Inventory.size:
                print("You have reached the maximum inventory capacity.")
                t.sleep(n)
                return 0
            else:
                Inventory.inventory[f'{item}'] = amount
                print(f'Added {amount} {item} to your inventory.')
                t.sleep(n)

def drop_item(item, rarity, amount, n):
    item = input("Enter type of item (health potion, mana potion, gold, book, scrap): ").lower().strip()       # update for future items
    if item in no_rarity:
        if f'{item}' not in Inventory.inventory.keys():
            print("That item is not in your inventory.")
            return 0
    else:
        if f'{rarity.lower()} {item}' not in Inventory.inventory.keys():
            print("That item is not in your inventory.")
            return 0
    if item in no_rarity:
        pass
    else:
        rarity = input("Enter the rarity (pitiful, bad, subpar, normal, good, epic, legendary, perfect): ")
        if rarity not in rarity_names:
            print("That is not a valid rarity.")
            return 0
    if item not in no_rarity:
        try:
            if Inventory.inventory[f'{rarity} {item}'] <= 0:
                print("You cannot drop that item.")
                t.sleep(n)
            else:
                Inventory.inventory[f'{rarity} {item}'] -= 1
                print(f'Removed {amount} {rarity} {item} to your inventory.')
                t.sleep(n)
                if Inventory.inventory[f'{rarity} {item}'] <= 0:
                    Inventory.inventory.pop(f'{rarity} {item}')
                    
        except Exception:
            print("You do not have that item.")
            t.sleep(n)
    else:
        try:
            if Inventory.inventory[f'{item}'] <= 0:
                print("You cannot drop that item.")
                t.sleep(n)
            else:
                Inventory.inventory[f'{item}'] -= amount
                print(f'Removed {amount} {item} to your inventory.')
                t.sleep(n)
                if Inventory.inventory[f'{item}'] <= 0:
                    Inventory.inventory.pop(f'{item}')
                    
        except Exception:
            print("You do not have that item.")
            t.sleep(n)

def print_inventory():
    #Inventory.inventory = dict(sorted(Inventory.inventory, key=o.itemgetter(0)))
    # i am not introducing sorting the inventory. ever. (okay maybe)
    if Inventory.inventory == {}:
        print("Your inventory is empty.")
    Inventory.inventory = dict(sorted(Inventory.inventory.items(), key=lambda x:x[0]))
    for key in Inventory.inventory.keys():
        print(f'{key}: {Inventory.inventory[key]}')
    """
    print(Inventory.inventory)
    for item in Inventory.inventory:
        print(item)
    Inventory.inventory = dict(Inventory.inventory)
    """