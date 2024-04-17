from cellcreation import *
from inventory import *
import time as t

#loot = ["hp_pot", "mn_pot", "gold", "book", "trash"] change whilst new items are being added
loot = ["hp_pot", "mn_pot", "gold", "book"]
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

book_rarities = {
    "minimum": 0,
    "blank": 100,
    "overrated": 200,
    "bad": 365,
    "normal": 765,
    "knowledgeable": 930,
    "intellectual": 989,
    "philosophical": 999,
    "wisdom": 1000
}
book_rarity_names = ["minimum",
    "blank",
    "overrated",
    "bad",
    "normal",
    "knowledgeable",
    "intellectual",
    "philosophical",
    "wisdom"
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
    
    
class Object:
    turn_amount = 1     # will be used for extra loot chances in a later update
    amount = 1 #placeholder for hp_pot and mn_pot functionality

class hp_pot(Object):
    loot_chance = 10    #default 10
    pitiful = 3
    bad = 5
    subpar = 7
    normal = 10
    good = 15
    epic = 25
    legendary = 40
    perfect = 100
    cell_spawn = True

class mn_pot(Object):
    loot_chance = 8    #default 8
    pitiful = 2
    bad = 4
    subpar = 7
    normal = 10
    good = 15
    epic = 20
    legendary = 30
    perfect = 50
    cell_spawn = True

class gold(Object):
    loot_chance = 50     # default 50
    min_amt = 1         # default 1
    max_amt = 5         # default 5
    cell_spawn = True

class book(Object):
    loot_chance = 2     #default 2
    cell_spawn = True
    amount = 1

class scrap(Object):
    loot_chance = 30        # default 30
    min_amt = 1             # default 1
    max_amt = 3             # default 3
    cell_spawn = True

loot = [hp_pot, mn_pot, gold, book, scrap]
no_rarity_items = list(["gold", "scrap"])

def no_rarity(item, n):
    num_add = r.randint(item.min_amt, item.max_amt)
    print(f'You got {num_add} {item.__name__}!')
    t.sleep(n)
    add_item(loot_names[f'{item.__name__}'], None, num_add, n)

def book_rarity(n):
    num = r.randint(1, 1000)
    for chance in range(1, len(book_rarities)):
        #print(rarity_names[chance-1])
        if num >= book_rarities[book_rarity_names[chance-1]] and num < book_rarities[book_rarity_names[chance]]:
            #print(f'Added a {rarity_names[chance]} {loot_names[item].lower()} to your inventory.')
            add_item(loot_names["book"], book_rarity_names[chance], book.amount, n)
            break
        else:
            continue

def pots_rarity(item, n):
    num = r.randint(1, 1000)
    for chance in range(1, len(rarities)):
        #print(rarity_names[chance-1])
        if num >= rarities[rarity_names[chance-1]] and num < rarities[rarity_names[chance]]:
            #print(f'Added a {rarity_names[chance]} {loot_names[item].lower()} to your inventory.')
            add_item(loot_names[item], rarity_names[chance], Object.amount, n)
            break
        else:
            continue
    

def loot_cell_intro(x, y, n):
    rarity_gen_item = None
    print("Generating item...") # more preserving pain here
    t.sleep(n)
    item_generated = False
    while item_generated == False:
        for item in loot:
            #chance = f'{item}.loot_chance'
            #print(int(f'{item}'__dict__.values()))
            #print(hp_pot.loot_chance)
            chance = r.randint(1, 100)
            lootchance = item.loot_chance
            amount = item.amount
            #print(chance)
            #print(item.__name__, str(lootchance), chance)
            #if r.randint(1, 100) <= item.__name__.loot_chance:
            if chance <= lootchance:
                rarity_gen_item = item.__name__
                if rarity_gen_item in no_rarity_items:
                    pass
                else:
                    print(f'You got {amount} {loot_names[item.__name__].lower()}!')
                t.sleep(n)
                cells[f'({x}, {y})'] = "normal"
                item_generated = True
                break
            else:
                continue
    if rarity_gen_item == "hp_pot" or rarity_gen_item == "mn_pot":
        eval(f'pots_rarity(rarity_gen_item, n)')
    elif rarity_gen_item in no_rarity_items:
        eval(f'no_rarity(item, n)')
    else:
        eval(f'{rarity_gen_item}_rarity(n)')
