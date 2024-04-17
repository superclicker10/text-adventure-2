from lootgeneration import *
from inventory import *

rarity_names = ["minimum",
    "pitiful",
    "bad",
    "subpar",
    "normal",
    "good",
    "epic",
    "legendary",
    "perfect"]

no_rarity_list = ["gold", "scrap"]
loot = ["health potion", "mana potion", "gold", "book", "scrap"]
potions = ["health potion", "mana potion"]

def use_item(Player, n):
    item = input("What type of item do you want to use? (health potion, mana potion, gold, book, scrap): ").lower().strip()
    if item not in loot:
        print("That is not a valid item.")
        t.sleep(n)
        return 0
    if item not in no_rarity_list:
        rarity = input("What rarity to use? (pitiful, bad, subpar, normal, good, epic, legendary, perfect): ").lower().strip()
    if item not in no_rarity_list:
        if f'{rarity} {item}' not in Inventory.inventory:
            print("You don't have that item.")
            t.sleep(n)
            return 0
    else:
        if f'{item}' not in Inventory.inventory:
            print("You don't have that item.")
            t.sleep(n)
            return 0
    if item in potions and (item not in no_rarity_list):
        eval(f'potions_use(item, rarity, Player, n)')
    elif item not in no_rarity_list:
        eval(f'book_use(rarity, Player, n)')
    else:
        eval(f'no_rarity(item, Player, n)')

def potions_use(item, rarity, Player, n):
    name = rarity
    if item == "health potion":
        backup = Player.health
        increase = eval(f'hp_pot.{name}')
        Player.health += increase
        Player.health = round(Player.health, 2)
        if Player.health >= Player.max_health:  # case if new health > max
            increase -= int(Player.health - Player.max_health)
            if increase <= 0:
                increase = 0
            Player.health = Player.max_health
            print(f'You now have {Player.health} ({backup}+{increase}) health.')
        else:
            print(f'You now have {Player.health} ({backup}+{increase}) health.')
    elif item == "mana potion":
        backup = Player.mana
        increase = eval(f'mn_pot.{name}')
        Player.mana += increase
        Player.mana = round(Player.mana, 2)
        if Player.mana >= Player.max_mana:  # case if new health > max
            increase -= float(Player.mana - Player.max_mana)
            if increase <= 0:
                increase = 0
            Player.mana = Player.max_mana
            print(f'You now have {Player.mana} ({backup}+{increase}) mana.')
        else:
            print(f'You now have {Player.mana} ({backup}+{increase}) mana.')
    t.sleep(n)
    Inventory.inventory[f'{rarity} {item}'] -= 1
    if Inventory.inventory[f'{rarity} {item}'] == 0:
        Inventory.inventory.pop(f'{rarity} {item}')

def book_use(rarity, Player, n):
    print("You can't use books right now.")
    t.sleep(n)
    # regen all health+mana, lore, spells, buffs, combining spells

def no_rarity(item, Player, n):
    print("You can't use this item currently.")
    t.sleep(n)
    
