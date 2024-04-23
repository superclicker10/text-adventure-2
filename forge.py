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

def merge_items(item, rarity, amount, n):
    for temp in range(0, len(rarity_names)):
        if rarity_names[temp] == rarity:
            pos = temp
            break
    rarity_to_merge = rarity_names[pos+1]
    temp1 = Inventory.inventory[f'{rarity} {item}']   
    temp2 = amount*requirements[rarity_to_merge] 
    if temp1 < temp2:      #add requirements for merging
        print(f"You don't have enough of that item to merge it (have {temp1}, need {temp2})")
        t.sleep(n)
        return 0
            
    Inventory.inventory[f'{rarity} {item}'] -= amount*requirements[rarity_to_merge]
    if Inventory.inventory[f'{rarity} {item}'] <= 0:
        Inventory.inventory.pop(f'{rarity} {item}')
    print(f'Merged into {amount} {rarity_names[pos+1]} {item}!')
    t.sleep(n)
    add_item(item, rarity_names[pos+1], amount, n) #add merging multiple items at once.