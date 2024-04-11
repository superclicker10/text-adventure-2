from cellcreation import *
from inventory import *
import time as t

#loot = ["hp_pot", "mn_pot", "gold", "book", "trash"] change whilst new items are being added
loot = ["hp_pot", "mn_pot"]
loot_names = {
    "hp_pot": "Health potion",
    "mn_pot": "Mana potion",
    "gold": "Gold",
    "book": "Book",
    "scrap": "Scrap"
    }

rarities = {        #cumulative system
    "minimum": 0,
    "pitiful": 80,
    "bad": 230,
    "subpar": 430,
    "normal": 780,
    "good": 930,
    "epic": 985,
    "legendary": 999,
    "perfect": 1000
}
rarity_names = ["minimum",
    "pitiful",
    "bad",
    "subpar",
    "normal",
    "good",
    "epic",
    "legendary",
    "perfect"]
    
    
class Object:
    pass

class hp_pot(Object):
    loot_chance = 10    #default 10
    cell_spawn = True

class mn_pot(Object):
    loot_chance = 8    #default 8
    cell_spawn = True

class gold(Object):
    loot_chance = 50
    cell_spawn = True

class book(Object):
    loot_chance = 2
    cell_spawn = True

class trash(Object):
    loot_chance = 30
    cell_spawn = True

loot = [hp_pot, mn_pot]

def pots_rarity(item, n):
    num = r.randint(1, 1000)
    for chance in range(1, len(rarities)):
        #print(rarity_names[chance-1])
        if num >= rarities[rarity_names[chance-1]] and num <= rarities[rarity_names[chance]]:
            #print(f'Added a {rarity_names[chance]} {loot_names[item].lower()} to your inventory.')
            add_item(loot_names[item], rarity_names[chance], n)
            break
        else:
            continue
    

def loot_cell_intro(x, y, n):
    rarity_gen_item = None
    print("Generating item...") # more preserving pain here
    t.sleep(n)
    for item in loot:
        #chance = f'{item}.loot_chance'
        #print(int(f'{item}'__dict__.values()))
        #print(hp_pot.loot_chance)
        chance = r.randint(1, 100)
        lootchance = item.loot_chance
        #print(item.__name__, str(lootchance), chance)
        #if r.randint(1, 100) <= item.__name__.loot_chance:
        if chance <= lootchance or item.__name__ == loot[-1].__name__:
            rarity_gen_item = item.__name__
            print(f'You got a {loot_names[item.__name__].lower()}!')
            t.sleep(n)
            cells[f'({x}, {y})'] = "normal"
            break
        else:
            continue
    if rarity_gen_item == "hp_pot" or rarity_gen_item == "mn_pot":
        eval(f'pots_rarity(rarity_gen_item, n)')
